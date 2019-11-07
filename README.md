# tubes_algeo_2
Halo, kami dari kelompok YouIYouX dan ini adalah hasil pengerjaan tugas besar 2 mata kuliah aljabar linear dan geometri.

## Installation
Download python3 dan pip dari website resmi python, lalu download database gambar yang disebutkan pada spesifikasi tugas. Ubah nama folder PINS menjadi PICS, dan pastikan Anda sudah men-delete folder PINS yang ada di dalamnya. Jika Anda ingin menambahkan foto, buat folder untuk gambar orang tersebut pada folder PICS dengan format "pin_<nama_orang>" dan masukkan fotonya di dalam folder itu. Jangan lupa untuk membuat folder DB untuk database hasil ekstraksi nantinya.

Lalu setelah folder PICS dan DB sudah siap, lakukan random sampling dengan cara yang disebutkan di bawah. Dari random sampling, akan dibuat 2 folder baru (atau di-delete dan dibuat baru), yaitu DataSet yang berisi folder gambar orang untuk referensi dan DataUji yang berisi folder gambar orang untuk pengujian, dengan rasio sesuai spesifikasi tugas. Kemudian, lakukan generate database (DB) dengan cara yang disebutkan di bawah untuk membuat database hasil ekstraksi pada DB/final.

Sekarang dengan data referensi, data uji, dan database yang sudah tersedia, Anda dapat melakukan tes akurasi, tes uji gambar, atau menampilkan GUI utama untuk melakukan face recognization sesuai keinginan Anda.

## Usage
### Cara menampilkan command
- Linux		:	python3 startapp.py
- Windows	:	python startapp.py

### Cara melakukan random sampling
- Linux		:	python3 startapp.py random-sample
- Windows	:	python startapp.py random-sample

### Cara men-generate database
- Linux		:	python3 startapp.py new-db
- Windows	:	python startapp.py new-db

### Cara men-generate database baru (dengan menyimpan database lama)
- Linux		:	python3 startapp.py new-db-with-hist
- Windows	:	python startapp.py new-db-with-hist

### Cara menampilkan GUI Utama
- Linux		:	python3 startapp.py run
- Windows	:	python startapp.py run

### Cara melakukan tes akurasi
- Linux		:	python3 startapp.py test-accuracy
- Windows	:	python startapp.py test-accuracy

### Cara melakukan tes uji gambar
- Linux		:	python3 startapp.py test-image
- Windows	:	python startapp.py test-image

## Used Libraries (with recommended version)
- Kivy 1.11.1
- gmpy2 2.0.8
- opencv-python 4.1.0.25
- numpy 1.17.0 