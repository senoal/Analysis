import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel ('provider_generate.xlsx')

# print(data.isnull().sum())
# print(data.head())

# munculkan jumlah data dari sebuah kolom
# data = data['provinsi'].str.replace(' ', '')
print(data['provinsi'].value_counts())

# pilih daerah dari kolom provinsi
sebuah_prov = input("Masukkan nama provinsi = ")
data = data.loc[data['provinsi']==sebuah_prov]

# munculkan jumlah data brand berdasarkan provinsi
print(data['brand'].value_counts())

brand_analis = data['brand']
# print(brand_kalimantan.value_counts())

simpati = brand_analis.loc[brand_analis == 'simPATI'].count()
a = simpati
kartuas = brand_analis.loc[brand_analis == 'kartuAS'].count()
kartuas_2 = brand_analis.loc[brand_analis == 'KartuAS'].count()
b = kartuas+kartuas_2
Loop = brand_analis.loc[brand_analis == 'Loop'].count()
Loop_2 = brand_analis.loc[brand_analis == 'LOOP'].count()
c = Loop+Loop_2
un_known = brand_analis.loc[brand_analis == 'UNKNOWN'].count()
d = un_known


# Terjemahkan data ke dalam plot
labels = 'simPATI', 'kartuAS', 'Loop', 'UNKOWN'
sizes = [a, b, c, d]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.05, 0.05, 0.05, 0.05)  # explode 1st slice

# Plot Daerah Bali
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=45)
plt.title('Distribusi Data ke '+sebuah_prov+'\n')
plt.axis('equal')
plt.show()