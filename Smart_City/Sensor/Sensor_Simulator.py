"""
Modul: Sensor Data Generator
Deskripsi: Modul ini berisi definisi class Sensor dan Location untuk mensimulasikan pengukuran kualitas udara dari berbagai jenis sensor (PM25, CO, Kebisingan).
Tanggal pembuatan: 16 April 2025
"""


import random
from datetime import datetime

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
    
class PM25Sensor(Sensor):
    """Kelas khusus untuk sensor partikulat PM2.5 yang mewarisi dari kelas Sensor."""

    def __init__(self, nama_sensor):
        """Inisialisasi sensor PM2.5."""
        super().__init__(nama_sensor, "sensor PM25")
    
    def analisis_kualitas(self):
        """Menganalisis kualitas udara berdasarkan kadar PM2.5."""
        if self.data_sensor is None:
            return "Data belum diupdate"
        
        if self.data_sensor <= 50:
            return "Baik"
        elif self.data_sensor <= 100:
            return "Sedang"
        else:
            return "Berbahaya"
    
    def get_info_sensor(self):
        """Mendapatkan informasi lengkap sensor PM2.5 termasuk analisis kualitas.

        Returns:
            str: String berisi informasi dasar sensor plus analisis kualitas udara.
        """
        info_dasar = super().get_info_sensor()
        if self.data_sensor is not None:
            return f"{info_dasar} | Kualitas: {self.analisis_kualitas()}"
        return info_dasar


class COSensor(Sensor):
    """Kelas khusus untuk sensor karbon monoksida (CO) yang mewarisi dari kelas Sensor."""

    def __init__(self, nama_sensor):
        """Inisialisasi sensor CO."""
        super().__init__(nama_sensor, "sensor CO")

    def cek_ambang_batas(self):
        """Memeriksa apakah kadar CO melebihi ambang batas aman."""
        if self.data_sensor is None:
            return "Data belum diupdate"
        
        if self.data_sensor <= 9:
            return "Aman"
        else:
            return "Berbahaya"

    def get_info_sensor(self):
        """Mendapatkan informasi lengkap sensor CO termasuk status ambang batas."""
        info_dasar = super().get_info_sensor()
        if self.data_sensor is not None:
            return f"{info_dasar} | Status: {self.cek_ambang_batas()}"
        return info_dasar


class NoiseSensor(Sensor):
    """Kelas khusus untuk sensor kebisingan yang mewarisi dari kelas Sensor."""

    def __init__(self, nama_sensor):
        """Inisialisasi sensor kebisingan."""
        super().__init__(nama_sensor, "sensor kebisingan")

    def analisis_kebisingan(self):
        """Menganalisis tingkat kebisingan berdasarkan nilai dB."""
        if self.data_sensor is None:
            return "Data belum diupdate"
        
        if self.data_sensor <= 55:
            return "Rendah"
        elif self.data_sensor <= 70:
            return "Normal"
        else:
            return "Tinggi"

    def get_info_sensor(self):
        """Mendapatkan informasi lengkap sensor kebisingan termasuk analisis tingkat."""
        info_dasar = super().get_info_sensor()
        if self.data_sensor is not None:
            return f"{info_dasar} | Tingkat: {self.analisis_kebisingan()}"
        return info_dasar

class Location:
    """Kelas untuk merepresentasikan suatu lokasi dengan beberapa sensor kualitas udara. """
    def __init__(self, kelurahan, kecamatan):
        """Inisialisasi lokasi dengan kelurahan dan kecamatan."""
        self.kelurahan = kelurahan
        self.kecamatan = kecamatan
        self.sensor_pm25 = PM25Sensor(f"PM25_{kelurahan}")
        self.sensor_co = COSensor(f"CO_{kelurahan}")
        self.sensor_kebisingan = NoiseSensor(f"NOISE_{kelurahan}")

    def update_all_sensors(self):
        """Memperbarui data semua sensor yang ada di lokasi ini."""
        self.sensor_pm25.update_data_sensor()
        self.sensor_co.update_data_sensor()
        self.sensor_kebisingan.update_data_sensor()

    def get_kualitas_udara(self):
        """Mendapatkan informasi lengkap kualitas udara di suatu lokasi."""
        self.update_all_sensors()
        info = f"Lokasi: {self.kelurahan}, {self.kecamatan}\n"
        info += f"1. {self.sensor_pm25.get_info_sensor()}\n"
        info += f"2. {self.sensor_co.get_info_sensor()}\n"
        info += f"3. {self.sensor_kebisingan.get_info_sensor()}"

        return info
