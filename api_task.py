import requests
import json

#Task1: Extract all senior roles and manager roles into a different list.
response = requests.get("https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo ")
response.status_code
remotejobs = response.json()
Senior_Role=[]
Manager_Role =[]
for details in remotejobs['jobs'][:]:
    if 'Senior' in details['jobTitle'] or details['jobLevel'] == 'Senior':
        Senior_Role.append(details['jobTitle'])
    elif 'Manager' in details['jobTitle']:
        Manager_Role.append(details['jobTitle'])


#Task2: Extract all the competition names into a separate list(competition_list)
response1 = requests.get("http://api.football-data.org/v4/competitions/")
response1.status_code
football = response1.json()
football_doc = football['competitions'][:]

competition_list = []
for c_names in football_doc:
    y= c_names['name']
    competition_list.append(y)



#Task3

response2 = requests.get("https://randomuser.me/api/?results=500")
response2.status_code
my_doc=response2.json()
my_new_doc = my_doc['results'][:]

#subtask1: Extracting all male and female profiles into a different list(male_profile and female profile)
male_profile=[]
female_profile =[]
for item in my_new_doc:
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


