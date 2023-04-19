import pandas as pd     
import numpy as np 
import glob as glob


Base=[]
def lectura_archivo(Base): 
    csv_files = glob.glob('Data/*.csv')
    for filename in csv_files:
        data = pd.read_csv(filename,sep=";")
        Base.append(data)
        
    return Base
Base=lectura_archivo(Base)

EAM08,EAM09,EMA10,EMA11,EMA12,EMA13,EMA14,EMA15,EMA16,EMA17,EMA18,EMA19,EMA20 = Base
Data_Merge= [EAM08,EAM09,EMA10,EMA11,EMA12,EMA13,EMA14,EMA15,EMA16,EMA17,EMA18,EMA19,EMA20]
missing = 0

def NullValues(Data_Merge,missing):
    for i in Data_Merge:
        for col in i.columns:
            missing += i[col].isna().sum()
        for row in i.index:
            missing += i.loc[row,:].isna().sum()

    print(missing)
    return missing

Missing = NullValues(Data_Merge,missing)


if __name__ == "__main__":
    lectura_archivo(Base)
    NullValues(Data_Merge,missing)
