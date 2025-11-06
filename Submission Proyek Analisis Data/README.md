🚀 Dashboard Analisis Kualitas Udara PRSA Aotizhongxin
Dashboard interaktif ini dibangun menggunakan Streamlit dan Python untuk menyajikan hasil Exploratory Data Analysis (EDA) dari dataset kualitas udara stasiun Aotizhongxin (Beijing), mencakup periode 2013 hingga 2017. Dashboard ini dirancang untuk menjawab pertanyaan bisnis terkait strategi pemasaran, persediaan, dan sistem peringatan dini berdasarkan tren polusi PM2.5 dan Ozon (O3).

📋 Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda memiliki perangkat lunak berikut terinstal:
- Python 3.8 atau versi yang lebih baru.
- Git (opsional, jika Anda mengkloning repositori).

🛠️ Persiapan Lingkungan
1. File Data
Pastikan file data berikut berada di direktori yang sama dengan file dashboard.py:
PRSA_Data_Aotizhongxin_20130301-20170228.csv (Dataset yang digunakan dalam analisis).

2. Instalasi Dependencies
Anda perlu menginstal library Python yang diperlukan.
pip install pandas matplotlib seaborn streamlit numpy

▶️ Cara Menjalankan Dashboard
Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi Streamlit secara lokal:

Langkah 1: Simpan Kode Aplikasi
Pastikan Anda telah menyimpan kode dashboard ke dalam file bernama dashboard.py.

Langkah 2: Navigasi ke Direktori
Buka Terminal (atau Command Prompt / PowerShell) dan navigasi ke direktori tempat Anda menyimpan dashboard.py dan file CSV.
C:\Users\Niel\Documents\DICODING\SUBMISSION 1 DATA SCIENCE\Submission Proyek Analisis Data\Dashboard> streamlit run dashboard.py

Langkah 3: Jalankan Aplikasi
Gunakan perintah streamlit run diikuti dengan nama file aplikasi:
streamlit run app_eda_only.py

Langkah 4: Akses Dashboard
Setelah perintah dijalankan, Streamlit akan membuka browser web Anda secara otomatis. Jika tidak, Anda dapat mengakses dashboard secara manual melalui alamat berikut:
Local URL: http://localhost:8501

📊 Fitur Dashboard
Dashboard ini menyediakan visualisasi interaktif utama yang mendukung insight bisnis:
- Tren Musiman PM2.5: Menunjukkan bulan-bulan dengan polusi tertinggi (puncak di Musim Dingin) untuk memandu strategi Persediaan dan Pemasaran.

- Tren Harian PM2.5 & O3: Mengidentifikasi jam-jam puncak polusi harian untuk mengoptimalkan waktu iklan dan aktivitas outdoor.

- Heatmap Korelasi: Memvisualisasikan hubungan antara PM2.5 dengan faktor cuaca (Kecepatan Angin (WSPM) dan Titik Embun (DEWP)) sebagai dasar Sistem Peringatan Dini sederhana.

- Filter Tahun: Memungkinkan pengguna untuk melihat tren harian untuk tahun tertentu atau rata-rata dari semua tahun.