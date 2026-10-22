# Tugas Data Mining — Eksplorasi Dataset Harga Rumah

## Deskripsi
Proyek ini merupakan tugas awal Data Mining menggunakan Python dan Pandas. Program membaca dataset harga rumah, mengeksplorasi struktur data, membagi kolom berdasarkan tipe penyimpanan, serta menghitung baris duplikat dan nilai kosong (*null*).

## Dataset
Gunakan dataset **House Prices: Advanced Regression Techniques** dari Kaggle.

- Tautan: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
- Unduh file `train.csv` dari bagian Data.
- Dataset pelatihan memiliki 1.460 baris dan 81 kolom pada versi standar kompetisi.

**Penting:** Dataset tidak disertakan dalam repositori ini. Unduh sendiri dari Kaggle dan letakkan `train.csv` di folder proyek. Perhatikan ketentuan lisensi dan aturan penggunaan dataset dari sumbernya.

## Isi repositori
- `data_mining.py` — program Python untuk menjalankan analisis.
- `data_mining.ipynb` — notebook dengan langkah analisis dan kode.
- `requirements.txt` — daftar dependensi Python.
- `ringkasan_kualitas_data.csv` — akan dibuat otomatis setelah program dijalankan.

## Persyaratan
- Python 3.9 atau lebih baru
- pandas

Pasang dependensi:

```bash
pip install -r requirements.txt
```

## Cara menjalankan script
Simpan `train.csv` di folder proyek, lalu jalankan:

```bash
python data_mining.py
```

Program akan menampilkan:
1. Lima baris pertama dataset.
2. Ukuran dataset dan informasi tipe data.
3. Kolom kategorikal dan numerikal.
4. Jumlah baris duplikat.
5. Jumlah nilai null total dan per kolom.
6. Statistik deskriptif.
7. File `ringkasan_kualitas_data.csv`.

## Cara menjalankan notebook
Buka `data_mining.ipynb` menggunakan Jupyter Notebook, JupyterLab, atau Google Colab. Unggah `train.csv` ke direktori kerja notebook, kemudian jalankan sel secara berurutan.

## Catatan interpretasi
Pemisahan kategorikal/numerikal awal dilakukan berdasarkan tipe data Pandas. Beberapa kolom numerik yang berisi kode kategori (contohnya `MSSubClass`) mungkin lebih tepat dianalisis sebagai kategori berdasarkan arti kolomnya. Nilai duplikat dan null yang aktual ditentukan dengan menjalankan program pada file dataset yang digunakan.

## Referensi
- McKinney, Wes. *Python for Data Analysis*, 3rd Edition. O'Reilly Media, 2022.
- Dokumentasi Pandas: https://pandas.pydata.org/docs/
- Kaggle — House Prices: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
