import requests

url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise"

headers = {
    'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
    'x-rapidapi-key': "7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf"
    }

response = requests.request("GET", url, headers=headers)

data=response.json()

for i in range(len(data)):
    id=data[i]["id"]
    name=data[i]["name"]
    case=data[i]["cases"]
    print(f"{id},{name},{case}")
    
    
    