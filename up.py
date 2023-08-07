import pandas as pd     
import numpy as np 
import glob as glob
import matplotlib.pyplot as plt

# Ejemplo de Data_Merge
data_merge_1 = pd.DataFrame({
    'CIIU': [1001, 1002, 1003, 1002, 1001],
    'WORKERS': [50, 30, 20, 40, 25]
})

data_merge_2 = pd.DataFrame({
    'CIIU': [2001, 2002, 2003, 2002, 2001],
    'WORKERS': [70, 50, 30, 60, 40]
})

Data_Merge = [data_merge_1, data_merge_2]

# Ejemplo de Data_Gruop
data_gruop_1 = pd.DataFrame({
    'CIIU': [1001, 1002, 1003],
    'SUM-WORKERS': [40, 30, 15]

})

data_gruop_2 = pd.DataFrame({
    'CIIU': [2001, 2002, 2003],
    'SUM-WORKERS': [80, 50, 30]
})

Data_Gruop = [data_gruop_1, data_gruop_2]



for i, df in enumerate(Data_Gruop):
    df.set_index("CIIU", inplace=True)




for i, df in enumerate(Data_Gruop):
        for index in df.index:
            if index in Data_Merge[i]["CIIU"].unique():               
                Numerator = Data_Merge[i][Data_Merge[i]["CIIU"] == index]["WORKERS"]
                Denominator = df["SUM-WORKERS"]
                Total = (Numerator / Denominator) * 100

