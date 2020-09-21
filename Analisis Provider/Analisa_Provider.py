import pandas as pd
import matplotlib.pyplot as plt

# periksa data
data = pd.read_excel ('provider.xlsx')
print(data.head(5))
print(data.shape)

non_hvc_ = data.loc[data['jenis'] == 'Non HVC'].count()
a = non_hvc_.loc['jenis']

platinum = data.loc[data['jenis'] == 'Platinum'].count()
b = platinum.loc['jenis']

gold = data.loc[data['jenis'] == 'Gold'].count()
c = gold.loc['jenis']

diamond = data.loc[data['jenis'] == 'Diamond'].count()
d = diamond.loc['jenis']

# Terjemahkan data ke dalam plot
labels = 'Non HVC', 'Platinum', 'Gold', 'Diamond'
sizes = [a, b, c, d]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.07, 0.03, 0.04, 0.02)  # explode 1st slice

# Plot Keseluruhan
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('-Persentase Data Total-\n')
plt.axis('equal')
plt.show()
df_total = pd.DataFrame(data['jenis'].value_counts())
print('Data Keseluruhan\n',df_total)

# Ambil data daerah (Bali)
bali = data.loc[data['provinsi']=='BALINUSRA']
# bali
# bali['jenis'].value_counts()

import matplotlib.pyplot as plt

# ambil data dari masing-masing 'jenis' level provider
data_bali = bali
non_hvc_bali = data_bali.loc[data_bali['jenis'] == 'Non HVC'].count()
e = non_hvc_bali.loc['jenis']

platinum_bali = data_bali.loc[data_bali['jenis'] == 'Platinum'].count()
f = platinum_bali.loc['jenis']

gold_bali = data_bali.loc[data_bali['jenis'] == 'Gold'].count()
g = gold_bali.loc['jenis']

diamond_bali = data_bali.loc[data_bali['jenis'] == 'Diamond'].count()
h = diamond_bali.loc['jenis']

# Terjemahkan data ke dalam plot
labels = 'Non HVC', 'Platinum', 'Gold', 'Diamond'
sizes = [e, f, g, h]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.07, 0.04, 0.04, 0.02)  # explode 1st slice

# Plot Daerah Bali
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Persentase Data Daerah Bali')
plt.axis('equal')
plt.show()

df_bali = pd.DataFrame(data_bali['jenis'].value_counts())
print('Data Daerah Bali\n',df_bali)