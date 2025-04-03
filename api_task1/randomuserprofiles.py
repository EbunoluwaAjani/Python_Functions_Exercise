import requests
import pandas as pd
import boto3
import os
from dotenv import load_dotenv
import awswrangler as wr

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')



response2 = requests.get("https://randomuser.me/api/?results=500")
response2.status_code
my_doc=response2.json()
my_new_doc = my_doc['results'][:]

#subtask1: Extracting all male and female profiles into a different list(male_profile and female profile)
male_profile=[]
female_profile =[]
gender = []
for item in my_new_doc:
    gender.append(item['gender'])
    if item['gender'] == 'male':
        male_profile.append(item)
    elif item['gender'] == 'female':
        female_profile.append(item)
    
#subtask2: Extract all dob date into a list(date_list).
date_list=[]
for item in my_new_doc:
    date_list.append(item['dob']['date'])

#subtask3:
full_name = []
for names in my_new_doc:
    first_name = names['name']['first']
    last_name = names['name']['last']
    concat_name = first_name + ' '+ last_name
    full_name.append(concat_name)

randomuserprofile={'full_name':full_name,
    'gender':gender,
                   'dob':date_list
    
}

df4 =pd.DataFrame(randomuserprofile)

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name= "eu-central-1")

wr.s3.to_parquet(
    df=df4,
    path= "s3://apitest-by-ebun/api_tasks/randomuserprofiles",
    boto3_session=session,
    mode='append',
    dataset=True
)