import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Perbaiki jalur file menggunakan raw string
file_path = r'csv_files\Full_Data_CTD_tanggal12.csv'  # Ganti dengan lokasi file Anda

# Baca file CSV dengan delimiter ';' dan tanpa header jika perlu
data = pd.read_csv(file_path, delimiter=';', header=0)

# Debug: Cetak nama kolom untuk memastikan kolom tersedia
print("Columns in dataset:", data.columns)

# Pastikan nama kolom sesuai
data.rename(columns=lambda x: x.strip(), inplace=True)  # Hilangkan spasi tak terlihat di kolom
time_column = 'Time'  # Ubah sesuai nama kolom yang dicetak

# Konversi kolom waktu
data[time_column] = pd.to_datetime(data[time_column], format='%H:%M:%S.%f', errors='coerce')

# Filter data hanya untuk rentang waktu antara jam 04:00 hingga 11:00
data_filtered = data[(data[time_column].dt.hour >= 4) & (data[time_column].dt.hour <= 11)]

# Konversi kolom numerik
numerical_columns = ['Depth', 'Pressure', 'Temperature', 'Conductivity', 
                     'Salinity', 'SoundVelocity', 'Density']
for col in numerical_columns:
    data_filtered[col] = pd.to_numeric(data_filtered[col], errors='coerce')

# Visualisasi data: Buat satu figure per grafik
for column in numerical_columns:
    plt.figure(figsize=(10, 6))
    plt.plot(data_filtered[time_column], data_filtered[column], label=column)
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.title(f'{column} vs Time (12 Oktober 2024)')
    
    # Atur format sumbu X untuk hanya menunjukkan jam
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # Hanya menampilkan jam dan menit
    plt.gca().xaxis.set_major_locator(mdates.HourLocator())  # Set locator untuk setiap jam
    
    plt.xticks(rotation=45)  # Rotasi label sumbu X agar lebih mudah dibaca
    plt.grid()
    plt.legend()
    plt.show()
