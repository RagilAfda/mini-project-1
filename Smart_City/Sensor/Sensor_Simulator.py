"""
Modul: Sensor Data Generator
Deskripsi: Modul ini berisi definisi class Sensor dan Location untuk mensimulasikan pengukuran kualitas udara dari berbagai jenis sensor (PM25, CO, Kebisingan).
Tanggal pembuatan: 16 April 2025
"""


import random

class Sensor:
    """
    Class untuk merepresentasikan sebuah sensor kualitas udara.

    Atribut:
        nama_sensor : Nama sensor.
        jenis_sensor : Jenis sensor (PM25, CO, Kebisingan).
        data_sensor : Data hasil pengukuran sensor.
    """
    def __init__(self, nama_sensor, jenis_sensor):
        """Inisialisasi atribut dan generate data sensor."""
        self.nama_sensor = nama_sensor
        self.jenis_sensor = jenis_sensor
        self.data_sensor = self.generate_data()
   
    def __init__(self, nama_sensor, jenis_sensor):
        """Inisialisasi sensor dengan nama dan jenis."""
        self.nama_sensor = nama_sensor
        self.jenis_sensor = jenis_sensor
        self.data_sensor = None
    
    def kadar_co(self):
        """Mengenerate kadar CO secara acak dalam satuan ppm."""
        nilai = round(random.uniform(0.1, 50.0), 2)
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai CO tidak valid: {nilai}")
        return nilai
    
    def partikular_udara(self):
        """Mengenerate kadar partikulat (PM2.5) secara acak."""
        nilai = random.randint(10, 200)
        if not (0 <= nilai <= 500):
            raise ValueError(f"Nilai PM2.5 tidak valid: {nilai}")
        return nilai
    
    def kebisingan(self):
        """Mengenerate tingkat kebisingan secara acak dalam satuan dB."""
        nilai = random.randint(40, 100)
        if not (30 <= nilai <= 150):
            raise ValueError(f"Nilai kebisingan tidak valid: {nilai}")
        return nilai

    def update_data_sensor(self):
        """Memperbarui data sensor berdasarkan jenis sensor."""
        if self.jenis_sensor == "sensor CO":
            self.data_sensor = self.kadar_co()
        elif self.jenis_sensor == "sensor PM25":
            self.data_sensor = self.partikular_udara()
        elif self.jenis_sensor == "sensor kebisingan":
            self.data_sensor = self.kebisingan()
    
    def get_info_sensor(self):
        """Mendapatkan informasi dasar dari sensor."""
        if self.data_sensor is None:
            return f"{self.nama_sensor} - Data belum diupdate"
        return f"{self.nama_sensor}: {self.data_sensor}"

class Location:
    """
    Class untuk merepresentasikan lokasi pemantauan kualitas udara.

    Atribut:
        kelurahan : Nama kelurahan.
        kecamatan : Nama kecamatan.
        sensor_pm25 : Objek sensor PM25.
        sensor_co : Objek sensor CO.
        sensor_kebisingan : Objek sensor Kebisingan.
    """
    def __init__(self, kelurahan, kecamatan, sensor_pm25, sensor_co, sensor_kebisingan):
        """Inisialisasi data lokasi dan sensor-sensornya."""
        self.kelurahan = kelurahan
        self.kecamatan = kecamatan
        self.sensor_pm25 = sensor_pm25
        self.sensor_co = sensor_co
        self.sensor_kebisingan = sensor_kebisingan

    def get_quality_info(self):
        """Mengembalikan informasi kualitas udara dari semua sensor di lokasi."""
        return (
            f"Lokasi: {self.kelurahan}, {self.kecamatan}\n"
            f"  - {self.sensor_pm25.get_info()} {chr(181)}g/m{chr(179)}\n"
            f"  - {self.sensor_co.get_info()}PPM\n"
            f"  - {self.sensor_kebisingan.get_info()}dB\n"
        )
