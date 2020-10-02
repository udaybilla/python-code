#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request as ur
import re
import sys
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError


# In[2]:


from datetime import date
today = date.today()
import time


# In[ ]:





# In[3]:



red_flags = ["data engineer", "statistician"] #List of words to avoid in job title
#required = ["software"] #Can also check for required words

def qualifies(title):
    title = title.lower()
    #Define a function to check if a job title is worth checking out  
    for word in red_flags:
        if word in title: return False
    return True

#test:
qualifies("data scientist")


# In[1]:


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


# In[4]:


# cities = ['dallas', 'austin', 'houston', 'tampa', 'orlando', 'miami', 'seattle', 'denver', 'philadelphia', 'pittsburgh', 'cleveland',  'atlanta','phoenix', 'charlotte', 'nashville', 'chicago', 'omaha', 'portland', 'los+angeles', 'san+antonio', 'kansas+city'
#          , 'columbus', 'St.+Louis', 'cincinnati','tucson', 'Salt+Lake+City']


# In[ ]:


import glob

path = r's3://indeedoutput' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
scrapedcompanies = []
if len(all_files)>0:
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    scrapedcompanies = frame['company'].unique().tolist()


# In[ ]:





# In[2]:


scrapedlinks = []

tuplelinks = []
counter =0

# Now define the Regex, 
# 1. Should not have the phrase 1+ years, 1-2 Years, so on..
p1 = re.compile('[2-9]\s*\+?-?\s*[1-9]?\s*[yY]e?a?[rR][Ss]?')
# 2. Should not have mention of "Citizenship", "Citizens", so on..
p2 = re.compile('[Cc]itizens?(ship)?')
p3 = re.compile('[Cc]learance')

t1 = p1.search("2+ Years of experiencce")
t2 = p1.search("0-1 Year")
#print (t1, "\n",t2)

#The first page with search results
place = 'united%20states'
url_base = "https://www.indeed.com/jobs?q=data+scientist&l="+place+"&jt=fulltime&sort=date&start=0"
#print(url_base)
pgno = 0
try:
        response = ur.urlopen(url_base+str(pgno))
        html_doc = response.read()
except:
        print("URL not accesible")
        exit();
soup = BeautifulSoup(html_doc, 'html.parser')
"Ready."


try:
    total_results = soup.find(id="searchCountPages").get_text()
    #print(total_results)
    last_page = int(int(total_results[total_results.index("of")+2: total_results.index("jobs")].strip().replace(',',"")) / 10) * 10
    #print(last_page)
except Exception as ex:
    print(ex)
    print ("No jobs found")

#print(last_page)

jobs_per_page = 10
#goodlinks = []

for pgno in range(0,last_page,jobs_per_page):
    if pgno > 0:
        try:
            response = ur.urlopen(url_base+str(pgno))
            html_doc = response.read()
        except:
            break;
        soup = BeautifulSoup(html_doc, 'html.parser')
    for job in soup.find_all(class_='result'):
        #print('inner for')
        link = job.find(class_="turnstileLink")
        try:
            jt = link.get('title')
        except:
            jt = ""
        try:
            comp = job.find(class_='company').get_text().strip()
        except:
            comp = ""
        
        if comp in scrapedcompanies:
            #print (comp, ' present')
            continue
            
        if(qualifies(jt.lower())):
            #print(jt, ' ', comp)
            toVisit = "http://www.indeed.com"+link.get('href')
            try:
                html_doc = ur.urlopen(toVisit).read().decode('utf-8')
            except:
                continue;
            #m = p1.search(html_doc)
            n = p2.search(html_doc)
            p = p3.search(html_doc)
            if not n and not p:
                #print(jt,",",comp,":",toVisit,"\n")
                if toVisit not in scrapedlinks:
                    tuplelinks.append((place, jt, comp, toVisit))
                    #print((place, jt, comp))
                    counter = counter+1
                scrapedlinks.append(toVisit)
                scrapedcompanies.append(comp)
                
                #print('counter')
                
                #goodlinks.append(toVisit)

    #print('befor csv ', counter)
    if counter > 100:
        #print('done ', place)
        #print('no of jobs ', len(tuplelinks))
        dfObj = pd.DataFrame(tuplelinks, columns = ['place' , 'jobtitle', 'company' , 'link'])
        filename = place+str(int(round(time.time() * 1000))) + '_' + str(today) + '_jobs.csv'
        dfObj.to_csv(filename)

        ACCESS_KEY = ''
        SECRET_KEY = ''
        uploaded = upload_to_aws(filename, 'indeedoutput', filename)

        tuplelinks=[]
        counter =0
#scrapedcompanies.to_csv('scraped_companies.csv')


# In[ ]:


len(scrapedlinks)


# In[ ]:





# In[ ]:





# In[ ]:




