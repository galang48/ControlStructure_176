def penilaian_siswa(persen_nilai):
    if persen_nilai >= 90:
        return "Excellent performance"
    elif persen_nilai >= 80:
        return "Very Good performance"
    elif persen_nilai >= 70:
        return "Good performance"
    elif persen_nilai >= 60:
        return "Average performance"
    else:
        return "Below average performance"


def angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def angka_fibonacci(n):
    urutan_fibonacchi = [0, 1]
    for i in range(2, n):
        urutan_fibonacchi.append(urutan_fibonacchi[i - 1] + urutan_fibonacchi[i - 2])
    return urutan_fibonacchi[:n]


def angka_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")


def perulangan(n):
    for i in range(1, n + 1):
        print(str(i) * i)


# Penilaian siswa
persen_nilai = int(input("Masukan persentase nilai: "))
hasil = penilaian_siswa(persen_nilai)
print(hasil)

# Mencari angka terbesar
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
hasil = angka_terbesar(a, b, c)
print(f"Largest number is: {hasil}")

# Mencetak angka Fibonacci
n = int(input("Masukan nilai N untuk deret fibonacci: "))
urutan_fibonacchi = angka_fibonacci(n)
print("angka_Fibonacci series:", urutan_fibonacchi)

# Mencetak angka ganjil
n = int(input("Masukan nilai N untuk bilangan ganjil: "))
print("Angka Ganjil Hingga angka", n, "adalah: ")
angka_ganjil(n)

# Perulangan angka
n = int(input("Masukan nilai N untuk pola segitiga: "))
perulangan(n)
