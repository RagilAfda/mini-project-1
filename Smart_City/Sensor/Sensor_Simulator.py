"""
Nama Modul : Sensor_Simulator.py

Modul tentang menampilkan nilai acak mengenai kadar CO, partikulat
udara, dan tingkat kebisingan

Penulis: Ragil Afda Tripradana

Tanggal: 23 Maret 2025
"""


import random

class Sensor:
    def __init__(self, nama_sensor, jenis_sensor):
        self.nama_sensor = nama_sensor
        self.jenis_sensor = jenis_sensor
        self.data_sensor = self.generate_data()

    def generate_data(self):
        if self.jenis_sensor == "PM25":
            return round(random.uniform(0, 150), 2)  
        elif self.jenis_sensor == "CO":
            return round(random.uniform(0, 10), 2)  
        elif self.jenis_sensor == "Kebisingan":
            return round(random.uniform(30, 100), 2) 
        else:
            return 0

    def get_info(self):
        return f"{self.nama_sensor} ({self.jenis_sensor}): {self.data_sensor}"

class Location:
    def __init__(self, kelurahan, kecamatan, sensor_pm25, sensor_co, sensor_kebisingan):
        self.kelurahan = kelurahan
        self.kecamatan = kecamatan
        self.sensor_pm25 = sensor_pm25
        self.sensor_co = sensor_co
        self.sensor_kebisingan = sensor_kebisingan

    def get_quality_info(self):
        return (
            f"Lokasi: {self.kelurahan}, {self.kecamatan}\n"
            f"  - {self.sensor_pm25.get_info()} {chr(181)}g/m{chr(179)}\n"
            f"  - {self.sensor_co.get_info()}PPM\n"
            f"  - {self.sensor_kebisingan.get_info()}dB\n"
        )
