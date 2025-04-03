import boto3
import os
from dotenv import load_dotenv
import pandas as pd
import awswrangler as wr
from api2_task import extract


load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
API_KEY = os.getenv('API_KEY')
url1 = 'https://content.guardianapis.com/search?page=1&q="nigeria"&from-date=2025-01-01&api-key={API_KEY}'
df = extract(url1)

#df = pd.read_csv('api_doc2.csv')
#df2 = pd.read_csv('remotejobsrole.csv')
#df3 = pd.read_csv('football_competition.csv')
#df4 = pd.read_csv('randomuserprofiles.csv')

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name= "eu-central-1")

wr.s3.to_parquet(
    df=df,
    path= "s3://apitest-by-ebun/api_tasks/guardian_file/",
    boto3_session=session,
    mode='append',
    dataset=True
)
'''
wr.s3.to_parquet(
    df=df2,
    path= "s3://apitest-by-ebun/api_tasks/remotejobroles",
    boto3_session=session,
    mode='append',
    dataset=True
)


wr.s3.to_parquet(
    df=df3,
    path= "s3://apitest-by-ebun/api_tasks/footballcompetition",
    boto3_session=session,
    mode='append',
    dataset=True)

wr.s3.to_parquet(
    df=df4,
    path= "s3://apitest-by-ebun/api_tasks/randomuserprofiles",
    boto3_session=session,
    mode='append',
    dataset=True)
'''




