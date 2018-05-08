# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__=='__main__':
   title='__'
   brand='__'
   price='__'
   features='__'
   all_features=[]
   record=[]
   
# access the page
   r=requests.get('https://www.daraz.pk/solo-5-power-bank-10000-mah-white-romoss-mpg38013.html')
   if r.status_code==200:
       html=r.text
      # print(html)
       soup=BeautifulSoup(html,'lxml')
      #title
       title_section=soup.find('h1')
      #print(title_section)
       if(title_section):
        title=title_section.text
       # print(title)
      #brand
       brand_section=soup.select('.sub-title > a')
      #print(brand_section)
       if(brand_section):
          brand=brand_section[0].text
          
         # print(brand_section[0].text)
          
      #features
       feature_section=soup.select('.list ul > li')
       if(feature_section):
         for f in feature_section:
             all_features.append(f.text)
        # print(all_features)
         features='|'.join(all_features)
         #print(all_features)
         
      #price
       price_section=soup.select('.price > span')
       if(price_section and len(price_section) >1):
          price=price_section[1].text.replace(',','').strip()
          #print(price)
      
       record.append(title)
       record.append(brand)
       record.append(features)
       record.append(price)  
      # add the feature in csv file
       with open('result-data.csv','a+',encoding='utf-8') as file:
            file.write('title,brand,all_feature,price\n')
            file.write(','.join(record))
      
      

      



