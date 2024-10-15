# 1. Evaluasi Murid
print("Evaluasi Murid")
while True:
    # Meminta input dari pengguna untuk persentase nilai
    nilai = int(input("Masukkan persentase murid: "))
    # Mengevaluasi nilai yang dimasukkan
    if nilai >= 90:
        print("Excellent performance")
        break # Menghentikan loop jika kondisi terpenuhi
    elif nilai >= 80:
        print("Very Good performance")
        break # Menghentikan loop jika kondisi terpenuhi
    elif nilai >= 70:
        print("Good performance")
        break # Menghentikan loop jika kondisi terpenuhi
    elif nilai >= 60:
        print("Average performance")
        break # Menghentikan loop jika kondisi terpenuhi
    else:
        print("Below average performance")
print('\n') # Memisahkan output dari program lainnya


# 2. Program Angka Terbesar
print("2. Program Angka Terbesar")
# Mengambil tiga input angka dari pengguna
angka1 = int(input("Masukkan Angka Pertama: "))
angka2 = int(input("Masukkan Angka Kedua: "))
angka3 = int(input("Masukkan Angka Ketiga: "))
# Menentukan angka terbesar menggunakan if-elif-else
if angka1 >= angka2 and angka1 >= angka3:
    print("Angka", angka1, "merupakan angka terbesar")
elif angka2 >= angka1 and angka2 >= angka3:
    print("Angka", angka2, "adalah angka terbesar")
else:
    print("Angka", angka3, "merupakan angka terbesar")
print('\n') # Memisahkan output dari program lainnya


# 3. Program Fibonacci
print("3. Program Fibonacci")
# Meminta input jumlah angka dalam deret Fibonacci
fibonacci = int(input("Masukkan jumlah angka: "))
x, y = 0, 1 # Inisialisasi dua angka pertama dalam deret Fibonacci
for z in range(fibonacci):
    print(x, end=" ") # Mencetak angka Fibonacci
    x, y = y, x + y # Mengupdate nilai x dan y
print('\n') # Memisahkan output dari program lainnya


# 4. Program Angka Ganjil
print("4. Program Angka Ganjil")
# Meminta input batas atas angka
Odd = int(input("Mau sampai angka berapa?: "))
for o in range(1, Odd + 1):
    if o % 2 != 0: # Mengecek apakah angka ganjil
        print(o, end=" ") # Mencetak angka ganjil
print('\n') # Memisahkan output dari program lainnya


# 5. Program Pola
print("5. Program Pola")
# Meminta input tinggi pola dari pengguna
Pattern = int(input("Tinggi pola: "))
for s in range(1, Pattern + 1):
    print((str(s) + " ") * s) # Mencetak pola angka
print('\n') # Memisahkan output dari program lainnya
