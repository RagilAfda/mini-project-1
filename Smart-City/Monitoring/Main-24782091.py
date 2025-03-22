import sys
import Sensor_Simulator

sys.path.append('D:/projekgit/projek3/Smart-City/Sensor')

data = Sensor_Simulator.sensor_data()

print("Membuat data:")
print(f"Karbon Monoksida: {data['Kadar karbon monoksida (CO)']} ppm")
print(f"Partikular Udara: {data['Partikular udara µg/m³']} µg/m³")
print(f"Kebisingan: {data['Kebisingan']} dB")
