# Inisialisasi awal dengan nilai negatif agar loop berjalan pertama kali
angka = -1 

while angka < 0:
    angka = int(input("Masukkan angka: "))

    if angka < 0:
        print("Harus positif!")

print(f"Terima kasih! Angka yang kamu masukkan adalah: {angka}")
print("program selesai")

while True:
    angka = int(input("Masukkan angka: "))
    if angka >= 0:
        break # Keluar dari loop jika angka positif
    print("Harus positif!")