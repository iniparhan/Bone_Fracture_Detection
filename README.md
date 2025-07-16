# Bone Fracture Detection

Repositori ini berisi sistem deteksi patah tulang menggunakan Deep Learning berbasis Convolutional Neural Network (CNN). Proyek ini mencakup seluruh proses dari pemrosesan data X-ray, pelatihan model, hingga prediksi berbasis antarmuka web menggunakan **Streamlit**.

## Tujuan Proyek

* Membangun model klasifikasi binary untuk mendeteksi apakah sebuah X-ray menunjukkan kondisi patah tulang (*fractured*) atau tidak (*not fractured*).
* Menerapkan CNN pada dataset X-ray seluruh bagian tubuh (tungkai atas, bawah, panggul, lutut, punggung bawah, dsb.).
* Menyediakan antarmuka pengguna berbasis Streamlit agar pengguna dapat mengunggah gambar X-ray dan mendapatkan hasil prediksi.

## Struktur File

| Nama File / Folder      | Deskripsi                                                             |
| ----------------------- | --------------------------------------------------------------------- |
| `app.py`                | File utama untuk menjalankan aplikasi Streamlit                       |
| `notebook.ipynb`        | Notebook Jupyter untuk EDA, preprocessing, dan pelatihan model CNN    |
| `README.md`             | Dokumentasi proyek                                                    |

## Langkah Instalasi & Eksekusi

Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal:

### 1. Setup & Unduh Model dari Kaggle

1. **Buat akun Kaggle** di [https://www.kaggle.com](https://www.kaggle.com) *(jika belum memiliki)*.
2. **Dapatkan API Token Kaggle**:

   * Buka halaman profil > *My Account*
   * Scroll ke bawah, klik **"Create New API Token"**
   * File `kaggle.json` akan terunduh ke komputer kamu.
3. **Lihat isi file `kaggle.json`** menggunakan teks editor. Di dalamnya terdapat dua informasi penting:

   ```
   {
     "username": "your_kaggle_username",
     "key": "your_kaggle_api_key"
   }
   ```
4. Salin nilai `username` dan `key` tersebut ke dalam notebook `notebook.ipynb` di bagian yang disediakan agar dapat mengakses dataset dari Kaggle langsung via kode Python di Google Colab.

### 2. Pindahkan File Model

5. Setelah training selesai di Colab, **unduh file `model.h5`** ke komputermu.
6. Letakkan file `model.h5` **di direktori yang sama dengan `app.py`**.

### 3. Jalankan Aplikasi Streamlit

7. Buka terminal dan arahkan ke direktori proyek.
8. Jalankan aplikasi dengan:

```
python -m streamlit run app.py
```

## Preview

![Screenshot 1](images/Screenshot (491).png)

![Screenshot 2](images/Screenshot (492).png)

## Library yang Dibutuhkan

Untuk menjalankan aplikasi ini secara lokal, pastikan telah menginstal dependensi berikut:

```
pip install tensorflow numpy matplotlib seaborn opencv-python pillow streamlit
```
