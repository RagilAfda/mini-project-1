import sys

sys.path.append('D:/projekgit/projek3/Smart-City/Sensor')

import Sensor_Simulator

data = Sensor_Simulator.sensor_data()

print("Membuat data:")
print(f"Karbon Monoksida: {data['Kadar karbon monoksida (CO)']} ppm")
print(f"Partikular Udara: {data['Partikular udara µg/m³']} µg/m³")
print(f"Kebisingan: {data['Kebisingan']} dB")
