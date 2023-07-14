import pandas as pd
read_xlsx = pd.read_excel("excel.xlsx")
read_xlsx.to_csv("csv.csv", index = None, header = True)
dataframe = pd.DataFrame(pd.read_csv("csv.csv"))
print(dataframe) 

#Se realizo la converticion de un archivo xlsx a csv