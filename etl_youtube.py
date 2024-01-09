'''
Extracting and Transforming mostPopular videos (Trending videos) in US using Youtube API
'''
import os
import googleapiclient.discovery
import pandas as pd

def run_youtube_etl():
    def process_videos(response_item):
        videos = []
        for video in response_item:
            title = video['snippet']["title"]
            description = video["snippet"]["description"]
            publishedAt = video["snippet"]["publishedAt"]
            viewCount = video["statistics"]["viewCount"]
            video_info = {'title':title, "description":description, "publishedAt":publishedAt, "viewCount":viewCount}
            videos.append(video_info)
        return videos

    def get_popular_channel():
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyDLrDRHHFB2clcJ379vorWz7maaU2_qOl4"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.videos().list(
            part="contentDetails, snippet, statistics",
            chart="mostPopular",
            regionCode='US'
        )
        response = request.execute()
        video_list = process_videos(response['items'])

        while response.get('nextPageToken', None):
            request = youtube.videos().list(
                part="contentDetails, snippet, statistics",
                chart="mostPopular",
                regionCode='US',
                pageToken=response['nextPageToken']
            )
            response = request.execute()
            video_list.extend(process_videos(response['items']))

        return(video_list)


        df = pd.DataFrame(get_popular_channel())
        df.to_csv("Youtube_Popular_Videos.csv")