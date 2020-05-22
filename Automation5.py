#how to download image file from link or url using python

import requests
import bs4
import sys
import time
import shutil
import os
import concurrent.futures

start=time.perf_counter()

cd=os.getcwd()
cd=cd+"/output/"


read=requests.get("https://stocksnap.io/search/nature")
data=bs4.BeautifulSoup(read.text,"lxml")
x=data.find_all("img")
urls=x[3:]

def save_image(a):
     link=a.get("src")
     file_name=link.split("/")[-1]
     data=requests.get(link,stream=True)
     data.raw.decode_content=True
     with open(cd+file_name,"wb")as f1:
         shutil.copyfileobj(data.raw,f1)
         f1.close()
         


with concurrent.futures.ThreadPoolExecutor() as executor:
    results=executor.map(save_image,urls)



end=time.perf_counter()
print(f"time taken {round(end-start,2)}")
 
 
         

         
    




