# Ganti 'obin' dengan nama pendek Anda di sini
NAMA_BENAR = "obin"

print("===obin marsus : ===")
print()

# Langkah 1: Verifikasi Nama
while True:
    nama_input = input("obin marsus : ").strip().lower()
    
    if nama_input == NAMA_BENAR:
        print(f"Halo {nama_input.title()}! Selamat datang.")
        break
    else:
        print("silahkan coba lagi")
        print()

print()
print("=== LANJUT KE PROGRAM SELANJUTNYA ===")
print()

# Langkah 2: Input Angka untuk Tabel Perkalian
while True:
    try:
        angka = int(input("Masukkan angka: "))
        
        # Validasi agar angka antara 1 sampai 10
        if 1 <= angka <= 10:
            break
        else:
            print("  Masukkan angka antara 1 sampai 10!")
    except ValueError:
        print("  Input harus berupa angka!")

print()
print(f"Tabel Perkalian {angka}:")
print("-" * 20)

# Langkah 3: Menampilkan Tabel Perkalian
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")

print("-" * 20)
print("Program selesai.")