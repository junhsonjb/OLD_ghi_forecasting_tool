import pandas as pd

url = 'ORS_Impact_Score_2010_2013.csv'
df = pd.read_csv(url, skiprows=1)

countrydata = []

for i in range(3, 218):
    country = df.iloc[i, 0]
    row = [country]
    countrydata.append(row)