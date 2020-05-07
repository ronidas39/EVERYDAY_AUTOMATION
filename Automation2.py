import pandas as pd
df=pd.read_csv("sample.csv")
#delete unwanted columns
col=[]
for cols in df.columns:
    col.append(cols)
df.drop(columns=['eq_site_limit',
 'hu_site_limit',
 'fl_site_limit',
 'fr_site_limit',
 'tiv_2011',
 'tiv_2012',
 'eq_site_deductible',
 'hu_site_deductible',
 'fl_site_deductible',
 'fr_site_deductible',
 'point_latitude',
 'point_longitude',
 'construction',
 'point_granularity'],axis=1,inplace=True)
#rearrange columns
df_final=df[["statecode","policyID","county","line"]]
df_final.columns=["statecode","policyID","county_name","line"]
df_final.to_csv("final_output.csv",index=False)