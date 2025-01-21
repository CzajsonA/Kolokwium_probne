import pomiary

temp_c = 25
temp_f = pomiary.c_to_f(temp_c)
print(f"Temperatura: {temp_c}°C to {temp_f:.2f}°F")

wiatr_ms = 10
wiatr_kmh = pomiary.predkosc_wiatru(wiatr_ms)
print(f"Prędkość wiatru: {wiatr_ms} m/s to {wiatr_kmh:.2f} km/h")

cisnienie_hpa = 1013
cisnienie_mmhg = pomiary.cisnienie_atmosferyczne(cisnienie_hpa)
print(f"Ciśnienie atmosferyczne: {cisnienie_hpa} hPa to {cisnienie_mmhg:.2f} mmHg")

dane_pogodowe = [
    {"temperatura": 20, "wiatr": 5, "cisnienie": 1010},
    {"temperatura": 22, "wiatr": 6, "cisnienie": 1015},
    {"temperatura": 18, "wiatr": 4, "cisnienie": 1008},
]

suma_cisnienia_mmhg = sum(pomiary.cisnienie_atmosferyczne(dzien["cisnienie"]) for dzien in dane_pogodowe)
srednie_cisnienie_mmhg = suma_cisnienia_mmhg / len(dane_pogodowe)
print(f"Średnie ciśnienie atmosferyczne z trzech dni: {srednie_cisnienie_mmhg:.2f} mmHg")
