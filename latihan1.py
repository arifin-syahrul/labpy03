print("Nama : Arifin Syahrul Azhadi Harahap")
print("NIM  : 352310965")
print("Menampilkan bilangan acak yang lebih kecil dari 0.5")
import random

jumlah = int(input("Masukkan Nilai N : "))
a = 0

for i in range(jumlah):
    a +=1
    b = random.uniform(.0,.5)
    print("data ke:",a,"==>",b)

print("Selesai")
