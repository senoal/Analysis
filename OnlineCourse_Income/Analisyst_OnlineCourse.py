import pandas as pd

df = pd.read_excel('Rekap_OnlineCourse.xlsx')
print(df.head(10),'\n')

# Periksa kolom yang mengandung data kosong
# print(df.isnull().sum(),'\n')

# Hapus baris tidak digunakan
data = df.drop([0,1,1296])
#print(data.head())

# Ubah sebuah kolom menjadi index
data = data.set_index('Rekap Pengumpulan Tugas dan Quiz Bootcamp Data Science')
# print(data.head())

# Urutkan data berdasarkan = ....
data = data.sort_values(by='Rekap Pengumpulan Tugas dan Quiz Bootcamp Data Science')
#print(data.head())

# Periksa jumlah total peserta
total_peserta = len(data.index)
#print(total_peserta)

#print(df['Rekap Pengumpulan Tugas dan Quiz Bootcamp Data Science'])
# Buat nilai uang pendaftaran peserta online course
jaminan = 100000

# Buat rumus mencari total biaya terkumpul
total_jaminan = total_peserta * jaminan
#print(total_jaminan)

# Cari peserta lulus (lulus = 1, tidak lulus = 0)
jml_peserta_lolos = data['Unnamed: 29'].sum()
# Buat objek peserta lulus
y = jml_peserta_lolos
# Buat objek peserta tidak lulus
x = total_peserta - y

#print("Peserta lolos =",y)
#print("peserta tidak lolos =",x)

# Buat objek total uang kembali ke peserta lulus
total_uang_kembali = y * jaminan
money_l = total_uang_kembali
#print("Total biaya kembali ke peserta =",money_l)

# Buat objek uang tidak kembali ke peserta (income)
income = total_jaminan - money_l
#rint('Total pemasukan dalam online course ini =',income)

# Buat objek persentase jumlah peserta lulus
persentase = (total_uang_kembali/total_jaminan)*100
print(persentase)
# ubah objek ke bentuk int
persentase = int(persentase)
print(persentase)
# Buat objek persentase jumlah peserta tidak lulus
persen = 100 - persentase
print(persen)

#print(persen,'%')

print("_________Data Bersih (Ekspor ke Excel)_________")

# Masukkan data didapatkan ke dalam bentuk datafram
periksa = {
    'jumlah peserta (Orang)' : [total_peserta],
    'Biaya pendaftaran (Rp.)':[jaminan],
    'Total biaya (Rp.)':[total_jaminan],
    'Peserta lulus (Orang)' : [y],
    'Peserta tidak lulus (Orang)':[x],
    'Persentase jumlah peserta lulus (%)':[persen],
    'Persentase jumlah peserta tidak lulus (%)':[persentase],
    'Pendapatan (Rp.)':[income],
    'Biaya kembali ke peserta lulus (Rp.)':[total_uang_kembali]
    }
# Transformasi bentuk data
data = pd.DataFrame.from_dict(periksa).T
# Simpan data ke format excel
data.to_excel('Analisa Data Kompetisi X.xlsx')  
print(data)

# Membuat visualisasi data, import library
import matplotlib.pyplot as plt

# buat keterangan untuk masing-masing data
judul = ['Tidak Lulus', 'Lulus']
# Masukkan jumlah peserta
jumlah = x,y

# Buat judul untuk hasil visualisasi
title = "Data Peserta Akhir \n-Histogram-"
ttl = "Analysis Result (Histogram)"
ttl1 = "Analysis Result (Pie Chart)"
# Buat bar chart
plt.bar(judul, jumlah)

# Masukkan judul
plt.title(title)
# Masukkan nama label untuk masing-masing sumbu
plt.ylabel("jumlah")
plt.xlabel("kategori")
# Simpan hasil visualisasi
plt.savefig(ttl+".png")
# Cetak visualisasi
plt.show()
# Buat label masing-masing data
pieLabels = 'Tidak Lulus', 'Lulus'

# Masukkan data untuk membuat pie chart
populationShare = x, y
figureObject, axesObject = plt.subplots()
# Buat jarak pada pie
explodeTuple = (0.0, 0.1)
# Atur bentuk pie
axesObject.pie(populationShare, explode=explodeTuple,
               labels=pieLabels, autopct='%1.2f%%',
               startangle=90)
# Buat bentuk frame persegi panjang
axesObject.axis('equal')
# Buat judul untuk pie chart
title = 'Data Online Course\nApril 2020'
# Cetak judul
plt.title(title)
# Simpan file pie chart
plt.savefig(ttl1+'.png')
plt.show()
