import csv
from math import radians, sin, cos, atan2, sqrt

class Station:
    def __init__(self, id: str, latitude: float, longitude: float):
        """
        Erstellt eine Wetterstation.

        :param id: Die eindeutige ID der Station (int).

        :param latitude: Die geografische Breite der Station (float).
        :param longitude: Die geografische Länge der Station (float).
        :param data: Eine Liste der Daten, die für diese Station gespeichert wurden (z. B. Wetterdaten).
        """
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """
        Repräsentation der Station als String.

        :return: String-Repräsentation der Station.
        """
        return f"Station(id={self.id}, latitude={self.latitude}, longitude={self.longitude})"

# Funktion zur Berechnung der Entfernung (Haversine-Formel)
def haversine(lat1, lon1, lat2, lon2):
    """
    Berechnet die Entfernung zwischen zwei Punkten auf der Erde in Kilometern.

    :param lat1: Breite des ersten Punkts (float).
    :param lon1: Länge des ersten Punkts (float).
    :param lat2: Breite des zweiten Punkts (float).
    :param lon2: Länge des zweiten Punkts (float).
    :return: Entfernung in Kilometern (float).
    """
    R = 6378.14  # Erdradius in Kilometern

    # Koordinaten in Bogenmaß umrechnen
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine-Formel
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Liste der Stationen einlesen
def load_stations(filename):
    stations = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=["ID", "LATITUDE", "LONGITUDE", "ELEVATION", "STATE", "NAME", "GSN", "HCN", "WMO"])

        for row in reader:
            station = Station(
                id=row["ID"],
                latitude=float(row["LATITUDE"]),
                longitude=float(row["LONGITUDE"])
            )
            stations.append(station)
    return stations

# Stationen im Radius finden
def find_stations_within_radius(stations, latitude, longitude, radius):
    """
    Findet alle Stationen innerhalb eines bestimmten Radius um eine gegebene Koordinate.

    :param stations: Liste der Stationen.
    :param latitude: Geografische Breite des Mittelpunkts (float).
    :param longitude: Geografische Länge des Mittelpunkts (float).
    :param radius: Radius in Kilometern (float).
    :return: Liste der Stationen innerhalb des Radius.
    """
    result = []
    for station in stations:
        distance = haversine(latitude, longitude, station.latitude, station.longitude)
        if distance <= radius:
            result.append((station, distance))
    return result
