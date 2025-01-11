import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filecsv = 'D:/File Codingan/Python/Beginner/data.csv'
df = pd.read_csv(filecsv , usecols=['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'price','yr_built', 'city', 'country'])

mean_price = df['price'].mean()
median_price = df['price'].median()
max_price = df['price'].max()
min_price = df['price'].min()

print(df.head())

print("Statistik Deskriptif Harga Rumah: \n")
print("Rata-rata harga rumah:", mean_price)
print("Median harga rumah:", median_price)
print("Harga rumah tertinggi:", max_price)
print("Harga rumah terendah:", min_price)
print("")

sns.histplot(data=df, x= 'price', bins=30, kde=True, color='Blue')

plt.title("Hubungan ukuran Rumah (sqft_living) dan harga (price)")
plt.xlabel("Ukuran rumah (Sqft_living)")
plt.ylabel("Harga(price)")
plt.show()


