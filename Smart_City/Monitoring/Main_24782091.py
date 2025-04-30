"""
Modul: Main - Sistem Pemantauan Kualitas Udara
Deskripsi: Program utama untuk interaksi pengguna dalam menambahkan dan melihat data kualitas udara dari berbagai lokasi menggunakan class Sensor dan Location.
Tanggal pembuatan: 16 April 2025
"""
from sys import path
path.append('..\\projek3\\Smart_City')

from Sensor.Sensor_Simulator import Location, COSensor, PM25Sensor, NoiseSensor
from datetime import datetime, timedelta


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

    while True:
        print("\n=== SISTEM PEMANTAUAN KUALITAS UDARA ===")
        print("1. Tambah Lokasi Pemantauan")
        print("2. Lihat Status Semua Lokasi")
        print("3. Cari Lokasi")
        print("4. Riwayat sensor beberapa waktu terakhir")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        try:
            if pilihan not in ["1", "2", "3", "4", "5"]:
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
                print("\nRIWAYAT DATA SENSOR")

                if not daftar_lokasi:
                    print("Belum ada lokasi yang terdaftar!")
                    continue

                for i, lokasi in enumerate(daftar_lokasi):
                    print(f"{i+1}. {lokasi.kelurahan}, {lokasi.kecamatan}")
                try:
                    index_lokasi = int(input("Pilih lokasi (nomor): ")) - 1
                    if not (0 <= index_lokasi < len(daftar_lokasi)):
                        raise ValueError("Nomor lokasi tidak valid.")
                    lokasi_dipilih = daftar_lokasi[index_lokasi]
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                    continue

                jenis = input("Masukkan jenis sensor (sensor CO / sensor PM25 / sensor kebisingan): ").strip()
                if jenis not in ["sensor CO", "sensor PM25", "sensor kebisingan"]:
                    print("Jenis sensor tidak valid.")
                else:
                    print(f"\nMenampilkan data simulasi 1 menit terakhir (interval 10 detik) untuk {jenis} di lokasi {lokasi_dipilih.kelurahan}, {lokasi_dipilih.kecamatan}...\n")
                    riwayat_data.clear()
                    nilai_list = []

                    for i, data in enumerate(generator_data_sensor(jenis, durasi_menit=1, interval_detik=10)):
                        data["kelurahan"] = lokasi_dipilih.kelurahan
                        data["kecamatan"] = lokasi_dipilih.kecamatan
                        riwayat_data.append(data)
                        nilai_list.append(data["nilai"])
                        print(f"Data ke-{i+1}: {data['waktu']} | {data['jenis']} : {data['nilai']} | Lokasi: {data['kelurahan']}, {data['kecamatan']}")

                    if nilai_list:
                        print("\n--- RINGKASAN ---")
                        print(f"  Tertinggi : {max(nilai_list)}")
                        print(f"  Terendah  : {min(nilai_list)}")
                        print(f"  Rata-rata: {round(sum(nilai_list)/len(nilai_list), 2)}")
                        print(f"\nTotal data: {len(nilai_list)}")

            elif pilihan == "5":
                print("Program selesai. Sampai jumpa!")
                break

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()
