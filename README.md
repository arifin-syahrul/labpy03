# labpy03
Tugas Praktikum 3(Membuat latihan1.py, latihan2.py, program1.py pada modul perulangan)

Nama : Arifin Syahrul Azhadi Harahap

NIM  : 352310965

Kelas: IE.23.C.13

Dosen: Agung Nugroho, S.Kom., M.Kom.
_____________________________________________________________________________________________________________________________________________________________________________________________
# Latihan01.py

Gambar Flowchart pada latihan 1

![Flowchart Latihan1](https://github.com/user-attachments/assets/abf8e06f-2183-43a1-95e5-4eb8cf3d77f2)


Algoritma latihan 1
Menampilkan N bilangan acak yang lebih kecil dari 0,5, nilai N diisi pada saat runtime.

1. Mulai
2. Memasukan/ import fungsi RANDOM terlebih dahulu.
3. Deklarasi int, masukkan jumlah N :
4. Memasukan deskripsi kombinasi for untuk menyelesaikannya.
5. Mencetak data ke 1 sampai N dengan hasil nilai kurang dari 0,5.
6. Selesai

Rumus Program untuk Latihan 1

Ketikkan rumusnya seperti dibawah ini.

![latihan01 py](https://github.com/user-attachments/assets/adf05a1d-dc70-4538-b6a6-0158fa68e280)

kemudian klik Run untuk meihat hasil Program

![hasil latihan01 py](https://github.com/user-attachments/assets/d21046d9-d445-4b4e-b3d6-5e4af0798960)
__________________________________________________________________________________________________________________________________________________________________________________________
# Latihan02.py

Gambar Flowchart pada latihan 2

![Flowchart Latihan2](https://github.com/user-attachments/assets/da0ce2bd-4410-4c6b-984a-018d242bbec3)

Algoritma Latihan 2
1. Mulai
2. int max = 0 Fungsi dari max untuk mencari nilai tertinggi.
3. Menggunakan fungsi perulangan while true, hingga menampilkan perulangan sampai batas tertentu. While disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.
4. Memasukan bilangan integer pada "a".
5. Menggunakan fungsi if jika max kurang dari nilai a, maka max sama dengan a.
6. Mengunakan fungsi if jika nilai a adalah 0 maka fungsi break artinya perulangan berhenti jika menulis nilai 0.
7. Mencetak nilai paling terbesar setelah break, sehingga menampilkan nilai terbesar diantara bilangan tersebut dalam perulangan.
8. Selesai

Rumus Program untuk Latihan 2

Ketikkan Rumusnya seperti dibawah ini.

![latihan02 py](https://github.com/user-attachments/assets/44add58b-cf4f-481a-b867-9a79d331bcf7)

kemudian klik Run untuk meihat hasil Program

![hasil latihan02 py](https://github.com/user-attachments/assets/29bcef09-da5d-4033-af5c-18633fc47330)
__________________________________________________________________________________________________________________________________________________________________________________________
# Program01.py

Soal Latihan

Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba, pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.

Algoritma Program 1
Penyelesaian menggunakan for, if

1. Mula-mula masukkan modal usahanya yaitu a = 100000000
2. Gunakan perintah for m in range (1,9):, for ini untuk perulangan dari 1 sampai 8, kenapa menggunakan for, karena for ini perulangan yang terhitung. Pada skrip in range(1, 9) akan membentuk list perulangan yang berisi [1,2,3,4,5,6,7,8] dan 9 itu tidak termasuk, untuk membuktikan bawa perulangan ini hanya sampai 8 saja.
3. Lalu gunakan perintah if(m>=1 and m<=2): b=a*0. if pertama ini untuk menentukan laba bulan ke 1 dan ke 2. Masukkan variable lalu kalikan nilai (a) dengan data bulan 1 dan 2. lalu print("Laba bulan ke-", m, "sebesar:", b) untuk menampilkan hasil laba. Pada bulan pertama dan kedua belum mendapatkan laba maka hasilnya 0.
4. Lalu if(m>=3 and m<=4): c=a*0.1. if yang kedua ini untuk menentukkan laba bulan ke 3 dan ke 4. Masukkan variable lalu kalikan nilai (a) dengan data bulan 3 dan 4. Pada bulan ke 3 itu baru mendapatkan laba sebesar 1% berarti bulan ke 4 juga sama. Lalu cetak (m) dan (c), dengan perintah print("Laba bulan ke-", m, "sebesar:", c).
5. Kemudian if(m>5 and m<=7): d=a*0.5. if ketiga ini untuk menentukan laba bulan ke 5 sampai ke 7. Masukkan variable lalu kalikan nilai (a) dengan data bulan 5 sampai 7. Pada bulan ke 5 laba naik sebesar 5% berarti pada bulan ke 6 dan 7 kenaikkan labanya sama. Lalu cetak (m) dan (d), dengan perintah print ("Laba bulan ke-", m, "sebesar:", d).
6. Selanjutnya if(m==8): e=a*0.2. if keempat atau yang terakhir ini untuk menentukan laba bulan ke 8. Masukkan variabel lalu kalikan nilai (a) dengan data bulan 8. Pada laba bulan ke 8 ini menurun sebanyak 2%. Lalu cetak (m) dan (e) dengan perintah print ("Laba bulan ke-", m, "sebesar:", e).
7. Kemudian yang terakhir totalkan semua keseluruhan laba yaitu total = b+b+c+c+d+d+d+e.
8. lalu print("Total laba adalah : ", total), untuk menampilkan hasil keseluruhan laba dari bulan pertama sampai bulan kedelapan.
9. Selesai

Rumus Program untuk Program 1 (Praktikum 3)

Ketikkan rumusnya seperti dibawah ini.

![program1 py](https://github.com/user-attachments/assets/2049f30f-325d-4531-8704-165af74dfb90)

kemudian klik Run untuk meihat hasil Program

![hasil program01 py](https://github.com/user-attachments/assets/784cf37f-8173-4d2f-a809-ba7094b7825b)

# Selesai



