## Youtube_ETL_Airflow



<img width="946" alt="image" src="https://github.com/dataliew/Youtube_ETL_Airflow/assets/54056888/6a03801f-e496-4627-8486-4e2c20e1ccae">


## **Overview**

- Extracting data from Youtube API, Transforming data using Pandas, Loading data using Apache Airflow in Amazon EC2 and load it to Amazon S3  
- Get brief understanding of building data pipelines  
- Using Python code to go through ETL process  

## **Setup**

- Python 3.9  
- AWS EC2: Ubuntu(t2.micro)  
- Apache Airflow 2.7.2  

## **Data Processing**
1. Extracting  
- Extracted data of mostPopular videos (Trending videos) using Youtube API

2. Transforming  
- Selected columns that I am interested: title, description, publishedAt, viewCount

3. Loading  
- Setting virtual environment using AWS EC2 to run Apache Airflow  
- Build DAG in Apache Airflow to build data pipelines  
- Load csv file into AWS S3  


## **Conclusion**
- Gained insights and knowledge about data pipelines and ETL processes

## **Future Work**
- Build and manage more complex data pipelines with data modeling
- Build End-to-End process from building data pipeline to data analysis
