import pandas as pd
 
data = {
    'Nama': ['Ridwan', 'Jihyo', 'Rayna', 'Anita', 'Faiq', 'Jisoo', 'Alexa', 'Alex', "Kevin", 'Layla', "Rania", "Vincenzo", 'Axel', 'Dody', 'Radit'],
    'Age' : [20, 19, 20, 21, 19, 24, 18, 22, 25, 26, 27, 28, 21, 27, 23],
    'Gender' : ['Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', "Male", 'Male', "Male", "Male"],
    'Address' : ['Mandailing', 'Bandung', 'Jakarta','Mandailing', 'Jakarta', 'Bandung', 'Surabaya', 'Surabaya', 'Surabaya','Jakarta','Malang', 'Malang', 'Solo', 'Solo', "Jakarta"],
    'Tinggi' : [167, 155, 163, 157, 165, 154, 163, 165, 165, 162, 165, 166, 168, 164, 166]
}

df = pd.DataFrame(data)
filtered_df = df[(df['Age'] > 18) & (df['Tinggi'] > 155) & (df['Address'] == 'Jakarta')]
print("Data Mahasiswa PENS = \n", df)
print("Filtered Data Mahasiswa PENS = \n", filtered_df)
