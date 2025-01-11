import pandas as pd

filecsv = 'D:/File Codingan/Python/Beginner/data.csv'
df = pd.read_csv(filecsv , usecols=['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'price','yr_built', 'city', 'country'])

print(df.head())
