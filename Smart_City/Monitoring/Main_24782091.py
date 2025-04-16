from sys import path
path.append('..\\projekclone\\SmartCity')

from Sensor.Sensor_Simulator import Sensor, Location

def tampilkan_menu():
    print("\n=== Sistem Pemantauan Kualitas Udara ===")
    print("1. Tambah Data Lokasi")
    print("2. Tampilkan Semua Lokasi")
    print("3. Keluar")

lokasi_list = []

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        kelurahan = input("Masukkan nama kelurahan: ")
        kecamatan = input("Masukkan nama kecamatan: ")

        sensor_pm25 = Sensor(f"Sensor PM25 -", "PM25")
        sensor_co = Sensor(f"Sensor CO -", "CO")
        sensor_kebisingan = Sensor(f"Sensor Kebisingan -", "Kebisingan")

        lokasi_baru = Location(kelurahan, kecamatan, sensor_pm25, sensor_co, sensor_kebisingan)
        lokasi_list.append(lokasi_baru)
        print("\nData lokasi berhasil ditambahkan!")

    elif pilihan == "2":
            print("\n=== Data Kualitas Udara Semua Lokasi ===")
            for lokasi in lokasi_list:
                print(lokasi.get_quality_info())

    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan sistem ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
