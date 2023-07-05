#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib #for mail purpose


# In[2]:


# Connect to Website and pull in data

URL = 'https://www.amazon.in/Sony-Bravia-inches-Google-KD-43X74K/dp/B09WN2CVMY/ref=sr_1_3?keywords=sony%2B43&qid=1688537901&sr=8-3&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

print(soup1)


# In[3]:


#Just purify html

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)


# In[4]:


#Find title element by going to page inspect and select title

title_element = soup2.find(id="productTitle")
if title_element:
    title = title_element.get_text().strip()
    print(title)
else:
    print("Title element not found.")


# In[5]:


price = soup2.find(class_="a-offscreen").get_text()
print(price)


# In[6]:


# Clean up the data a little bit

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[7]:


# Create a Timestamp for your output to track when data was collected

today = datetime.date.today()

print(today)


# In[8]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraper.csv', 'w', newline='', encoding='UTF8') as E:
    writer = csv.writer(E)
    writer.writerow(header)
    writer.writerow(data)
    


# In[9]:


import pandas as pd

df = pd.read_csv(r'C:\Users\acer\AmazonWebScraper.csv')

print(df)


# In[10]:


#Now we are appending data to the csv

with open('AmazonWebScraper.csv', 'a+', newline='', encoding='UTF8') as E:
    writer = csv.writer(E)
    writer.writerow(data)


# In[11]:


def check_price():
    URL = 'https://www.amazon.in/Sony-Bravia-inches-Google-KD-43X74K/dp/B09WN2CVMY/ref=sr_1_3?keywords=sony%2B43&qid=1688537901&sr=8-3&th=1'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title_element = soup2.find(id="productTitle")
    title = title_element.get_text().strip() if title_element else "Title element not found."
    print(title)

    price_element = soup2.find(class_="a-offscreen")
    price = price_element.get_text().strip() if price_element else "Price element not found."
    print(price)

    price = price.strip()[1:]
    title = title.strip()

    import datetime
    today = datetime.date.today()

    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraper.csv', 'a+', newline='', encoding='UTF8') as E:
        writer = csv.writer(E)
        writer.writerow(data)


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(5)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\acer\AmazonWebScraper.csv)

print(df)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('AlexTheAnalyst95@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'AlexTheAnalyst95@gmail.com',
        msg

