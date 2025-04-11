"""
Nama Modul : Main-24782091.py

Modul utama untuk mengambil dan menampilkan data sensor dari modul
Sensor_Simulator

fitur utama: menampilkan output berupa nilai acak mengenai kadar CO,
partikulat udara, dan tingkat kebisingan

Penulis: Ragil Afda Tripradana

Tanggal: 23 Maret 2025
"""


from sys import path

path.append('..\\projek3')

from Smart_City.Sensor import Sensor_Simulator as sensor

def menu():
    while True:
        print("\n=== MENU PEMANTAUAN KUALITAS KOTA ===")
        print("1. Tambah Lokasi pemantauan")
        print("2. Tampilkan Kualitas Udara di semua lokasi")
        print("3. Cari Lokasi")
        print("4. Keluar")

        opsi = input("Pilih menu (1-4): ").strip()

        if opsi == "1":
            lokasi = input("Masukkan nama lokasi (format: kecamatan, kelurahan): ")
            hasil = sensor.tambah_lokasi(lokasi)
            print(hasil)

        elif opsi == "2":
            data = sensor.data_gabungan()
            if not data:
                print("Belum ada lokasi yang ditambahkan.")
            else:
                for lokasi, nilai in data.items():
                    print("===  Status Kualitas Kota  ===")
                    print(f"Lokasi: {lokasi}")
                    print(f"Karbon Monoksida: {nilai['Kadar CO']} ppm")
                    print(f"Partikular Udara: {nilai['Partikular udara']} µg/m³")
                    print(f"Kebisingan: {nilai['Kebisingan']} dB")
        
        elif opsi == "3":
            keyword = input("Masukkan kata kunci pencarian lokasi: ")
            result = sensor.cari_lokasi(keyword)
            if result:
                print("Lokasi ditemukan:")
                for loc in result:
                    print(f"> {loc}")
            else:
                print("Lokasi tidak ditemukan.")

        elif opsi == "4":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Input tidak valid. Silakan masukkan angka 1-4.")


if __name__ == "__main__":  # inisialisasi bahwa modul ini program utama
    menu()
