"""
Nama Modul : Sensor_Simulator.py

Modul tentang menampilkan nilai acak mengenai kadar CO, partikulat
udara, dan tingkat kebisingan

Penulis: Ragil Afda Tripradana

Tanggal: 23 Maret 2025
"""


import random


def kadar_co():  # kadar karbon monoksida
    """
    Deskripsi: Fungsi ini digunakan untuk menghasilkan kadar CO secara acak
    dalam satuan ppm.

    Type Data Parameter: Tidak memiliki parameter. Output yang dihasilkan
    Float.

    Nilai yang Dikembalikan: Mengembalikan nilai acak antara 0.1 hingga 50.0,
    dibulatkan hingga 2 angka dibelakang koma.
    """
    return round(random.uniform(0.1, 50.0), 2)


def partikular_udara():  # fungsi kualitas udara
    """
    Deskripsi: Fungsi ini digunakan untuk menghasilkan tingkat partikulat
    udara secara acak dalam satuan µg/m³ (mikrogram per meter kubik).

    Type Data Parameter: Tidak memiliki parameter. Output yang dihasilkan
    Integer.

    Nilai yang Dikembalikan: Mengembalikan nilai acak antara 10 hingga 200.
    """
    return random.randint(10, 200)


def kebisingan():  # fungsi tingkat kebisingan
    """
    Deskripsi: Fungsi ini digunakan untuk menghasilkan tingkat kebisingan
    secara acak dalam satuan dB (desibel).

    Type Data Parameter: Tidak memiliki parameter. Output yang dihasilkan
    Integer.

    Nilai yang Dikembalikan: Mengembalikan nilai acak antara 1 hingga 120.
    """
    return random.randint(1, 120)


def sensor_data():  # fungsi pengumpulan data
    """
    Deskripsi: Fungsi ini digunakan untuk mengumpulkan data dari tiga fungsi
    dan mengembalikannya dalam bentuk dictionary.

    Type Data Parameter: Tidak memiliki parameter. Output yang dihasilkan
    Dictionary.

    Nilai yang Dikembalikan: Mengembalikan nilai acak dari 3 fungsi sebelumnya.
    """
    co_level = kadar_co()
    oxygen_level = partikular_udara()
    noise_level = kebisingan()

    return {
        "Kadar CO": co_level,
        "Partikular udara": oxygen_level,
        "Kebisingan": noise_level
    }

lokasi_terdaftar = [] # list kosong untuk save lokasi

def tambah_lokasi(lokasi):
    """
    Menambahkan lokasi baru ke dalam daftar lokasi terdaftar.

    Argument: lokasi.

    Return: informasi pesan berhasil dan gagal.
    """
    lokasi = lokasi.strip().title()
    if not lokasi:  # kondisi input user kosong
        return "Lokasi tidak boleh kosong."
    if lokasi in lokasi_terdaftar:  # kondisi lokasi yang sama
        return f"Lokasi '{lokasi}' sudah terdaftar."
    lokasi_terdaftar.append(lokasi)
    return f"Lokasi '{lokasi}' berhasil ditambahkan."


def semua_lokasi():
    """
    Mengembalikan daftar semua lokasi yang telah terdaftar.

    Return: list yang berisi nama-nama lokasi
    """
    return lokasi_terdaftar  # berisi semua lokasi yang sudah terdaftar

def data_gabungan():
    """
    Mengembalikan dictionary berisi data kualitas udara untuk setiap lokasi terdaftar.
    
    Returns:
        dict: Format {lokasi: {"Kadar CO": float, "Partikular udara": int, "Kebisingan": int}}
    """
    data_lokasi = {}
    for lokasi in lokasi_terdaftar:
        data_lokasi[lokasi] = sensor_data()
    return data_lokasi


def cari_lokasi(keyword):
    """
    Mencari lokasi berdasarkan keyword yang diberikan user

    Argument: 
    keyword: kata kunci pencarian.

    Return: 
    list: daftar lokasi yang mengandung keywordnya.
    """
    keyword = keyword.strip().lower()
    hasil_pencarian = []  # inisialisasi
    for loc in lokasi_terdaftar:
        if keyword in loc.lower():
            hasil_pencarian.append(loc)

    return hasil_pencarian
