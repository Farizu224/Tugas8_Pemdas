import pandas as pd

# Kolom Data
# kolom = ['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'Kabupaten/Kota', 'Produksi_Sampah', 'satuan', 'Tahun']

# Membaca data CSV
df = pd.read_csv('Data Sampah/Data Sampah.csv')
# df.head()
# print(df)

# Nomer 2 itung jumlah sampah di tahun tertentu
df_2016=df[df['Tahun']==2016]
sampah_2016=df_2016['Produksi_Sampah'].sum()
print("Total sampah di 2016 jawa barat adalah: ",sampah_2016)

# Nomer 3 itung jumlah sampah per tahun
totalTahunan = df.groupby('Tahun')['Produksi_Sampah'].sum()
print("Total produksi sampah per tahun:")
print(totalTahunan)

# Nomer 4 itung jumlah sampah per kabupaten/kota per tahun per per
totalKotaTahun = df.groupby(['Kabupaten/Kota','Tahun'])['Produksi_Sampah'].sum ()
print("Total Produksi sampak kota per tahun: ")
print(totalKotaTahun)
