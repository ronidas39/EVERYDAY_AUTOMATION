import  io
import requests

response=requests.get("https://feeds.citibikenyc.com/stations/stations.json")
data=response.json()
#this will help you to understand the keys in the dictionary
print(set(data))
print(set(data["stationBeanList"][1]))

with io.open("stationlist.csv","w",encoding="utf-8")as f1:
    f1.write("ID"+","+"NAME"+","+"longitude"+"\n")
    for  i  in  range ( len ( data [ "stationBeanList" ])):
     id=data["stationBeanList"][i]["id"]
     name=data["stationBeanList"][i]["stationName"]
     longitude=data["stationBeanList"][i]["longitude"]
     data_row=str(id)+","+name+","+str(longitude)+"\n"
     f1.write(data_row)
    f1.close()