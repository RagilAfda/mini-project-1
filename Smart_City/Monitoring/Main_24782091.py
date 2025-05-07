"""
Modul: Main - Sistem Pemantauan Kualitas Udara
Deskripsi: Program utama untuk interaksi pengguna dalam menambahkan dan melihat data kualitas udara dari berbagai lokasi menggunakan class Sensor dan Location.
Tanggal pembuatan: 16 April 2025
"""
from sys import path
path.append('..\\projek3\\Smart_City')

from Sensor.Sensor_Simulator import Location, COSensor, PM25Sensor, NoiseSensor
from datetime import datetime, timedelta
import csv 


def generator_data_sensor(jenis, durasi_menit=1, interval_detik=10):
    """
    Generator untuk menghasilkan data sensor acak tiap interval dalam durasi tertentu.
    """
    sensor_map = {
        "sensor CO": lambda: COSensor("CO Simulasi"),
        "sensor PM25": lambda: PM25Sensor("PM25 Simulasi"),
        "sensor kebisingan": lambda: NoiseSensor("Noise Simulasi")
    }

    sensor = sensor_map[jenis]()
    waktu_awal = datetime.now() - timedelta(minutes=durasi_menit)
    waktu_saat_ini = waktu_awal

    while waktu_saat_ini <= datetime.now():
        sensor.update_data_sensor()
        yield {
            "waktu": waktu_saat_ini.strftime("%Y-%m-%d %H:%M:%S"),
            "jenis": jenis,
            "nilai": sensor.data_sensor
        }
        waktu_saat_ini += timedelta(seconds=interval_detik)

def main():
    daftar_lokasi = []
    riwayat_data = []
    riwayat_ringkasan = []

    while True:
        print("\n=== SISTEM PEMANTAUAN KUALITAS UDARA ===")
        print("1. Tambah Lokasi Pemantauan")
        print("2. Lihat Status Semua Lokasi")
        print("3. Cari Lokasi")
        print("4. Riwayat sensor beberapa waktu terakhir")
        print("5. Lihat Riwayat Ringkasan Sensor")
        print("6. Mengunduh data dalam bentuk CSV")
        print("7. Melihat file")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        try:
            if pilihan not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
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
                print("\nRIWAYAT DATA SENSOR UNTUK SEMUA JENIS SENSOR")

                if not daftar_lokasi:
                    print("Belum ada lokasi yang terdaftar!")
                    continue

                i = 1
                for lokasi in daftar_lokasi:
                    print(f"{i}. {lokasi.kelurahan}, {lokasi.kecamatan}")
                    i += 1

                try:
                    idx = int(input("Pilih lokasi (nomor): ")) - 1
                    lokasi = daftar_lokasi[idx]

                    jenis_sensor_list = ["sensor CO", "sensor PM25", "sensor kebisingan"]
                    ringkasan_lokasi = {
                        "lokasi": f"{lokasi.kelurahan}, {lokasi.kecamatan}",
                        "sensor": {}
                    }

                    for jenis in jenis_sensor_list:
                        print(f"\nData 1 menit terakhir tiap 10 detik untuk {jenis} di {lokasi.kelurahan}, {lokasi.kecamatan}:\n")
                        riwayat_data.clear()
                        nilai_list = []

                        j = 1
                        for data in generator_data_sensor(jenis, 1, 10):
                            data.update({
                                "kelurahan": lokasi.kelurahan,
                                "kecamatan": lokasi.kecamatan
                            })
                            riwayat_data.append(data)
                            nilai_list.append(data["nilai"])
                            print(f"Data ke-{j}: {data['waktu']} | {data['jenis']} : {data['nilai']} | Lokasi: {data['kelurahan']}, {data['kecamatan']}")
                            j += 1

                        if nilai_list:
                            ringkasan_lokasi["sensor"][jenis] = {
                                "maksimum": max(nilai_list),
                                "minimum": min(nilai_list),
                                "rata_rata": round(sum(nilai_list)/len(nilai_list), 2)
                            }

                    riwayat_ringkasan.append(ringkasan_lokasi)

                except (ValueError, IndexError):
                    print("Input tidak valid.")
            
            elif pilihan == "5":
                print("\n=== RINGKASAN RIWAYAT SENSOR ===")
                if not riwayat_ringkasan:
                    print("Belum ada data ringkasan yang tersimpan.")
                else:
                    i = 1
                    for r in riwayat_ringkasan:
                        print(f"\nRingkasan ke-{i}:")
                        print(f"Lokasi: {r['lokasi']}")
                        for jenis, nilai in r["sensor"].items():
                            print(f"- {jenis}:")
                            print(f"    Tertinggi : {nilai['maksimum']}")
                            print(f"    Terendah  : {nilai['minimum']}")
                            print(f"    Rata-rata : {nilai['rata_rata']}")
                        i += 1

            elif pilihan == "6":
                nama_file = input("Masukkan nama file CSV (misal: ringkasan.csv): ").strip()
                with open(nama_file, "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Lokasi", "Jenis Sensor", "Tertinggi", "Terendah", "Rata-rata"])
                    for data in riwayat_ringkasan:
                        lokasi = data['lokasi']
                        for jenis, nilai in data['sensor'].items():
                            writer.writerow([
                                lokasi,
                                jenis,
                                nilai['maksimum'],
                                nilai['minimum'],
                                nilai['rata_rata']
                                ])
                        print(f"Data ringkasan berhasil disimpan dalam file '{nama_file}'.")


            elif pilihan == "7":
                nama_file_unduhan = input("Masukkan nama yang telah di unduh")
                with open(nama_file_unduhan, "r") as file:
                    reader = csv.reader(file)
                    print("isi file")
                    for baris in reader:
                        print(baris)

            elif pilihan == "8":
                print("Program selesai. Sampai jumpa!")
                break

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()
