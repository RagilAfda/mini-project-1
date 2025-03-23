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

from Smart_City.Sensor import Sensor_Simulator

data = Sensor_Simulator.sensor_data()

print("Membuat data:")
print(f"Karbon Monoksida: {data['Kadar karbon monoksida (CO)']} ppm")
print(f"Partikular Udara: {data['Partikular udara µg/m³']} µg/m³")
print(f"Kebisingan: {data['Kebisingan']} dB")
