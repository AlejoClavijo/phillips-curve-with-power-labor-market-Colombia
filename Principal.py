import pandas as pd     
import numpy as np 
import glob as glob


Base=[]
csv_files = glob.glob('Data/*.csv')

for filename in csv_files:
    if filename == "Data\\EAM_2020.csv":
        print("ok")
        data = pd.read_csv(filename,sep=",")
        
    else:
        data = pd.read_csv(filename,sep=";")
      
    Base.append(data)


EAM_2020.head()