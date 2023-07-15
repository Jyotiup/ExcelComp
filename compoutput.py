import pandas as pd
import datetime
from csv import writer
import csv
import os

mypath=os.getcwd()
files = os.listdir(mypath)

compfile={}
comptask={}


for x in files:
    if (x[len(x)-4:len(x)])== "xlsx":
        c_time=os.stat(x).st_birthtime
        dt_c=datetime.datetime.fromtimestamp(c_time)
        df_xlsx = pd.read_excel(x,sheet_name=None)
        for sheet_name in df_xlsx.keys():
            df = df_xlsx[sheet_name]
            #print(f"{sheet_name} has {len(df.index)} rows")
            if sheet_name[0:5] != "Sheet" and sheet_name[0:5] != "Index":
                comptask[sheet_name]=len(df.index)
        compfile[str(dt_c)]=comptask
        comptask={}

            
compoutput=[]
dateandcount={}
for file in compfile:
    for task in compfile[file]:
        dateandcount["task"]=task
        dateandcount["date"]=file
        dateandcount["count"]=compfile[file][task]
        
        compoutput.append(dateandcount)
        dateandcount={}

df=pd.DataFrame(compoutput)
df.to_excel("raw_output.xlsx",index=False)
grouped=df.groupby('task')

try:
    os.remove("output.csv")
except:
    print("No Output File")

for task,date in grouped:
    #print(task)
    mytask=pd.Series(task)
    mytask.to_csv("output.csv",mode='a',index=False,header=False)
    myline="\n\n"
    ntask=pd.Series(myline)
    ntask.to_csv("output.csv",mode='a',index=False,header=False)
    #print(date)
    date.to_csv("output.csv",mode='a',index=False,header=True)
    myline="\n\n"
    ntask=pd.Series(myline)
    ntask.to_csv("output.csv",mode='a',index=False,header=False)
    myline="\n\n"
    ntask=pd.Series(myline)
    ntask.to_csv("output.csv",mode='a',index=False,header=False)
    
print("Job Completed!")