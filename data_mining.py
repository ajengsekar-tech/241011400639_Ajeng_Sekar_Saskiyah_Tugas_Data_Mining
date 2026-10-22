"""
Tugas Data Mining: Eksplorasi Dataset Harga Rumah
Referensi dataset: Kaggle - House Prices: Advanced Regression Techniques
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data

Letakkan file train.csv di folder yang sama dengan script ini, lalu jalankan:
    python data_mining.py
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path("train.csv")


def main():
    if not DATA_FILE.exists():
        print("File train.csv belum ditemukan.")
        print("Unduh train.csv dari Kaggle dan letakkan di folder yang sama dengan program ini.")
        print("Sumber: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data")
        return

    # 1. Data Loading
    df = pd.read_csv(DATA_FILE)
    print("=" * 60)
    print("1. DATA LOADING")
    print("=" * 60)
    print("Lima data pertama:")
    print(df.head())

    # 2. Eksplorasi Data
    print("\n" + "=" * 60)
    print("2. EKSPLORASI DATA")
    print("=" * 60)
    print(f"Jumlah baris: {df.shape[0]}")
    print(f"Jumlah kolom: {df.shape[1]}")
    print("\nInformasi dataset:")
    df.info()

    # 3. Membagi tipe data
    # Kolom object/category/string dianggap kategorikal berdasarkan tipe penyimpanan.
    # Kolom numerik dipisahkan berdasarkan tipe penyimpanan; kolom angka berkode kategori
    # seperti MSSubClass dapat ditinjau secara substantif dan diperlakukan sebagai kategori.
    categorical = df.select_dtypes(include=["object", "category", "string"])
    numerical = df.select_dtypes(include=["number"])

    print("\n" + "=" * 60)
    print("3. PEMBAGIAN DATA KATEGORIKAL DAN NUMERIKAL")
    print("=" * 60)
    print(f"Jumlah kolom kategorikal: {categorical.shape[1]}")
    print("Kolom kategorikal:")
    print(categorical.columns.tolist())
    print(f"\nJumlah kolom numerikal: {numerical.shape[1]}")
    print("Kolom numerikal:")
    print(numerical.columns.tolist())

    print("\nTipe data setiap kolom:")
    print(df.dtypes)

    # 4. Data duplikat dan null
    duplicate_count = int(df.duplicated().sum())
    null_by_column = df.isnull().sum()
    total_null = int(null_by_column.sum())

    print("\n" + "=" * 60)
    print("4. PEMERIKSAAN DUPLIKAT DAN NILAI NULL")
    print("=" * 60)
    print(f"Jumlah baris duplikat: {duplicate_count}")
    print(f"Total nilai null: {total_null}")
    print("\nKolom yang memiliki nilai null:")
    print(null_by_column[null_by_column > 0].sort_values(ascending=False))

    # 5. Statistik deskriptif
    print("\n" + "=" * 60)
    print("5. STATISTIK DESKRIPTIF")
    print("=" * 60)
    print("\nStatistik kolom numerikal:")
    print(df.describe())
    print("\nRingkasan kolom kategorikal:")
    print(df.describe(include="object"))

    # Simpan ringkasan kualitas data ke CSV untuk dokumentasi hasil aktual.
    summary = pd.DataFrame({
        "tipe_data": df.dtypes.astype(str),
        "jumlah_null": df.isnull().sum(),
        "jumlah_nilai_unik": df.nunique(dropna=True),
    })
    summary.to_csv("ringkasan_kualitas_data.csv", index_label="nama_kolom")
    print("\nRingkasan kualitas data disimpan ke ringkasan_kualitas_data.csv")


if __name__ == "__main__":
    main()
