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

    def generate_data(self):
        """Menghasilkan data acak berdasarkan jenis sensor."""
        if self.jenis_sensor == "PM25":
            return round(random.uniform(0, 150), 2)  
        elif self.jenis_sensor == "CO":
            return round(random.uniform(0, 10), 2)  
        elif self.jenis_sensor == "Kebisingan":
            return round(random.uniform(30, 100), 2) 
        else:
            return 0

    def get_info(self):
        """Mengembalikan informasi sensor dalam format string."""
        return f"{self.nama_sensor} ({self.jenis_sensor}): {self.data_sensor}"

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
