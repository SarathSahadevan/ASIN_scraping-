# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:40:43 2019

@author: Sarath.Sahadevan
"""
import requests

url_array = []
    
#from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import bs4
query = input("Search Here :")

res = requests.get('https://google.com/search?q={}'.format(query+'amazon'))
#res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElements = soup.select('.r a')
linkToOpen = min(7,len(linkElements))
for i in range(linkToOpen):
    url_array.append('https://google.com'+linkElements[i].get('href'))
  
asin_array = []
 
start = 'dp/'
end = '&'
for url in url_array:
    
    if len(url[url.find(start)+len(start):url.find(end)])== 10:
        
    
        asin_array.append(url[url.find(start)+len(start):url.find(end)])

