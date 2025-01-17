print("Moin")
import csv
# Datei öffnen
import csv
import station
import requests

# url = "https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/csv/ghcnd-stations.csv"
# response = requests.get(url)
# if response.status_code == 200:
#     with open('ghcnd-stations.csv', 'wb') as file:
#         file.write(response.content)

# Hauptlogik
if __name__ == "__main__":
    # CSV-Datei einlesen
    stations = station.load_stations('ghcnd-stations.csv')

    # Eingabe der Koordinate und des Radius
    latitude = float(input("Geben Sie die Breite (Latitude) ein: "))
    longitude = float(input("Geben Sie die Länge (Longitude) ein: "))
    radius = float(input("Geben Sie den Radius in Kilometern ein: "))

    # Stationen innerhalb des Radius finden
    nearby_stations = station.find_stations_within_radius(stations, latitude, longitude, radius)

    # Ergebnisse ausgeben
    print(f"\nStationen innerhalb von {radius} km um ({latitude}, {longitude}):")
    for station, distance in sorted(nearby_stations, key=lambda x: x[1]):
        print(f"{station} - Entfernung: {distance:.2f} km")




