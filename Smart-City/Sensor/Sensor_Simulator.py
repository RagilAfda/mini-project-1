import random

def kadar_co(): # kadar karbon monoksida
    return round(random.uniform(0.1, 50.0), 2)

def partikular_udara(): # fungsi kualitas udara
    return random.randint(10, 200)

def kebisingan(): # fungsi tingkat kebisingan
    return random.randint(40, 100)

def sensor_data():
    co_level = kadar_co()
    oxygen_level = partikular_udara()
    noise_level = kebisingan()
    
    return {
        "Kadar karbon monoksida (CO)": co_level,
        "Partikular udara µg/m³": oxygen_level,
        "Kebisingan": noise_level
    }
