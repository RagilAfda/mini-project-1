"""
Modul: Main - Sistem Pemantauan Kualitas Udara
Deskripsi: Program utama untuk interaksi pengguna dalam menambahkan dan melihat data kualitas udara dari berbagai lokasi menggunakan class Sensor dan Location.
Tanggal pembuatan: 16 April 2025
"""
from sys import path
path.append('..\\projek3\\Smart_City')

from Sensor.Sensor_Simulator import Location
from datetime import datetime, timedelta
import random

def generator_data_sensor(jenis, durasi_menit=1, interval_detik=30):
    """
    Generator untuk menghasilkan data sensor acak tiap interval dalam durasi tertentu.
    """
    waktu_awal = datetime.now() - timedelta(minutes=durasi_menit)
    waktu_saat_ini = waktu_awal
    while waktu_saat_ini <= datetime.now():
        data = {
            "waktu": waktu_saat_ini.strftime("%Y-%m-%d %H:%M:%S"),
            "jenis": jenis,
            "nilai": (
                round(random.uniform(0.1, 50.0), 2) if jenis == "sensor CO" else
                random.randint(10, 200) if jenis == "sensor PM25" else
                random.randint(40, 100)
            )
        }
        yield data
        waktu_saat_ini += timedelta(seconds=interval_detik)

def main():
    daftar_lokasi = []

    while True:
        print("\n=== SISTEM PEMANTAUAN KUALITAS UDARA ===")
        print("1. Tambah Lokasi Pemantauan")
        print("2. Lihat Status Semua Lokasi")
        print("3. Cari Lokasi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        try:
            if pilihan not in ["1", "2", "3", "4"]:
                raise ValueError("Pilihan tidak valid. Silakan pilih antara 1-4.")

            if pilihan == "1":
                print("\nTAMBAH LOKASI PEMANTAUAN")
                kelurahan = input("Masukkan nama kelurahan: ")
                kecamatan = input("Masukkan nama kecamatan: ")

                if not kelurahan.strip() or not kecamatan.strip():
                    raise ValueError("Nama kelurahan dan kecamatan tidak boleh kosong.")

                lokasi_baru = Location(kelurahan.strip(), kecamatan.strip())
                daftar_lokasi.append(lokasi_baru)
                print(f"Lokasi {kelurahan}, {kecamatan} berhasil ditambahkan!")

            elif pilihan == "2":
                print("\nSTATUS KUALITAS UDARA SEMUA LOKASI")
                if not daftar_lokasi:
                    print("Belum ada lokasi yang terdaftar!")
                else:
                    for lokasi in daftar_lokasi:
                        print("\n" + lokasi.get_kualitas_udara())
                        print("-----------------------------")

            elif pilihan == "3":
                print("\nCARI LOKASI")
                if not daftar_lokasi:
                    print("Belum ada lokasi yang terdaftar!")
                else:
                    keyword = input("Masukkan nama kelurahan/kecamatan: ").lower().strip()
                    ditemukan = False
                    for lokasi in daftar_lokasi:
                        if (keyword in lokasi.kelurahan.lower() or 
                            keyword in lokasi.kecamatan.lower()):
                            print("\n" + lokasi.get_kualitas_udara())
                            print("-----------------------------")
                            ditemukan = True
                    if not ditemukan:
                        print("Lokasi tidak ditemukan!")

            elif pilihan == "4":
                print("Program selesai. Sampai jumpa!")
                break

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()
