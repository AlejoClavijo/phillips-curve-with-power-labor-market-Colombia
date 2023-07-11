#Fragmento de codigo que se puede usar cuando se desee limpiar el CIIU

column_mapping = {"CIIU3": "CIIU", "ciiu3": "CIIU", "ciiu4": "CIIU", "ciiu_4": "CIIU", "CIIU4": "CIIU"}
for df in Data_Merge:
    df.rename(columns=column_mapping, inplace=True)


#################################################################################3
#Determina si los label de varios dataframe son todos iguales
#Data_Merge es una lista de dataframe
#item el item del label que vamos a comparar

def Existir (Data_Merge,item): 
    columna_presente = True
    for df in Data_Merge:
        if item not in df.columns:
            columna_resente = False
            print(f"La columna {item} no está presente en el DataFrame", i)

    if columna_presente:
        print(f"La columna {item} está presente en todos los DataFrames.")


###########################################################################

#Para verificar datos Nulos, en listas y columunas al mismo tiempo
missing_col=0
missing_row=0
for i in Data_Merge:
    for col in i.columns:
        missing_col += i[col].isna().sum()
    for row in i.index:
        missing_row += i.loc[row,:].isna().sum()
print(missing_col)
print(missing_row)

#Funcion para mirar si hay datos faltantes por colmuna
def exis_colum(Data_Merge,colum):
    missing_col=0
    for i in Data_Merge:
        missing_col += i[colum].isnull().sum()
    return missing_col


#Para mirar si hay datos faltantes por fila
def exis_row(Data_Merge,row):
    missing_row=0
    for i in Data_Merge:
        missing_row += i.loc[row,:].isna().sum()
    return missing_col


############################################################################

def type(Data_Merge,colum):
    for column in Data_Merge.columns:
        data_type = df[column].dtype
        print(f"La columna '{column}' tiene el tipo de dato '{data_type}'.")

###########################

#arr = pd.DataFrame({'A': [4, 2, 1, 3], 'B': [4, 2, 1, 3]})
#print(arr)
#def selection_sort(arr):
#    n = len(arr)
#    for i in range(n-1):
#        min_idx = i
#        for j in range(i+1, n):
#            if arr.iloc[j]["A"] < arr.iloc[min_idx]["A"]:
#                min_idx = j
#        arr.loc[[i,min_idx]]  = arr.loc[[min_idx, i]].values
#    return arr


#Ejemplo de uso
#sorted_data = selection_sort(arr)
#print(f"salida /n {sorted_data}")
#Problemas el CIIU es un codigo puede que no tenga mayores ni menores


#################33

#Proceso Inicial: 
for i, d in enumerate(Data_Merge):
    sorted_df = d.sort_values(by="CIIU")
    Data_Merge[i] = sorted_df 