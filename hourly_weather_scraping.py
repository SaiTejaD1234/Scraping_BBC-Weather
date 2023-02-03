import os
import requests
import json
from urllib.parse import urlencode
import numpy as np
import pandas as pd
import re  
from bs4 import BeautifulSoup
from datetime import datetime
import time

def location_id(c):
    location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
   'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
   's': c,
   'stack': 'aws',
   'locale': 'en',
   'filter': 'international',
   'place-types': 'settlement,airport,district',
   'order': 'importance',
   'a': 'true',
   'format': 'json'
    })
    p=requests.get(location_url).json()
    k=p['response']['results']['results'][0]['id']
    return k

def scrap(city):
  result=location_id(city)
  url      = 'https://www.bbc.com/weather/'+result
  response = requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser') 
  daily_high = soup.find_all('span', attrs={'class': 'wr-day-temperature__high-value'}) 
  daily_high_values = [daily_high[i].text.strip().split()[0] for i in range(0,13)]
  daily_low=soup.find_all('span', attrs={'class': 'wr-day-temperature__low-value'})
  daily_low_values =[daily_low[i].text.strip().split()[0] for i in range(0,13)]
  daily_summary = soup.find('div', attrs={'class': 'wr-day-summary'})
  daily_summary_list = re.findall('[a-zA-Z][^A-Z]*', daily_summary.text) 
  daily_summary_list=daily_summary_list[0:13]
  datelist = pd.date_range(datetime.today(), periods=len(daily_high_values)).tolist()
  datelist = [datelist[i].date().strftime('%y-%m-%d') for i in range(0,13)]
  weather={'Date':datelist,'High':daily_high_values,'Low':daily_low_values,'Summary':daily_summary_list}
  df = pd.DataFrame(weather)
  return df

city=input('enter a city: ')
weather=pd.DataFrame()
weather=scrap(city)

while 1>0:
  data=scrap(city)
  weather=weather.set_index('Date')
  weather.update(data.set_index('Date'))
  weather=weather.reset_index()
  weather=pd.concat([weather,data]).drop_duplicates().reset_index()
  weather=weather.drop(columns=['index'])
  print(weather)
  lines=weather.to_string()
  with open('weather.txt', 'w') as f:
    f.write(lines)
  time.sleep(3600)