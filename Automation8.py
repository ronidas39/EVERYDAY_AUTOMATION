import io
import pandas as pd
import json

df=pd.read_csv("stationlist.csv")
dc=df.to_dict(orient="index")
with io.open("output.json","w",encoding="utf-8")as f2:
    f2.write(json.dumps(dc,indent=4))
    f2.close()
        
