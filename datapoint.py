import requests

class DataPoint:
    def __init__(self, date: int, tmax: list, tmin: list, station=None):
        """
        Erstellt einen Datenpunkt mit Monat, Temperaturdaten und einer zugehörigen Station.

        :param date: Jahr+Monat im Format YYYYMM (z. B. 202401).
        :param station: Die Station (Instanz der Klasse Station), der dieser Datenpunkt zugeordnet ist.
        """

        self.date = date
        self.tmax = tmax
        self.tmin = tmin
        self.station = station  # Referenz einer Station

    def validate_date(self, date: int):
        """
        Überprüft, ob das Datum korrekt ist (YYYYMM).

        :param date: Datum im Format YYYYMM.
        :return: True, wenn das Datum korrekt ist, ansonsten False.
        """
        year = date // 100
        month = date % 100
        return 1 <= month <= 12 and year > 0

    def __repr__(self):
        """
        Repräsentation des Datenpunkts als String.

        :return: String-Repräsentation des Datenpunkts.
        """
        year = self.date // 100
        month = self.date % 100
        station_name = self.station if self.station else "None"
        return f"DataPoint(date={year}-{month:02d}, station='{station_name}, tmax={self.tmax}, tmin={self.tmin}')"

def extract_values(line: str) -> float:
    """
    Extrahiert die VALUE-Werte aus dem gegebenen String und berechnet den Durchschnitt.

    :param line: Der gegebene String mit den Daten.
    :return: Der Durchschnitt der VALUE-Werte.
    """
    # Leere Liste für die VALUE-Werte
    value_werte = []

    # Schleife über die Startpositionen der VALUE-Felder (22, 30, 38, ..., 262)
    for start in range(21, len(line), 8):  # Start ist 21, da Python 0-basiert ist
        value_str = line[start:start + 5].strip()  # 5 Zeichen für die VALUE-Werte (z.B. ' 267')

        if value_str.isdigit() or (value_str.startswith('-') and value_str[1:].isdigit() and value_str != '-9999'):
            # Wenn es eine gültige Zahl ist, konvertiere sie in eine Ganzzahl
            value_werte.append(int(value_str))

    # Berechnung des Durchschnitts
    if value_werte:
        durchschnitt = sum(value_werte) / len(value_werte) / 10
        return float(f"{durchschnitt:.2f}")
    else:
        return 0  # Falls keine gültigen Werte extrahiert wurden

def download_and_create_datapoints(station_id: str):
    """
    Lädt die Datei einer gegebenen Station-ID herunter, extrahiert die relevanten Zeilen und erstellt DataPoint-Objekte.

    :param station_id: Die Station-ID, um die Datei herunterzuladen (z. B. 'ACW00011604').
    """
    url = f"https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/all/{station_id}.dly"
    response = requests.get(url)

    if response.status_code == 200:
        file_name = f"{station_id}.dly"

        # Datei speichern
        with open(file_name, 'wb') as file:
            file.write(response.content)

        # Listen für Tmax und Tmin
        tmax_data = []
        tmin_data = []
        date = None

        # Jede Zeile der Datei durchgehen
        with open(file_name, 'r') as file:
            for line in file:
                if len(line) > 21 and (line[17:21] == "TMAX" or line[17:21] == "TMIN"):
                    # Extrahiere Datum (z.B. Jahr + Monat)
                    current_date = int(line[11:17])  # Jahr + Monat (YYYYMM)

                    # Wenn es eine TMAX Zeile ist, hole die Temperaturdaten
                    if line[17:21] == "TMAX":
                        tmax_data.append(extract_values(line))
                    elif line[17:21] == "TMIN":
                        tmin_data.append(extract_values(line))

                    # Falls die Tmax und Tmin für den gesamten Monat extrahiert sind, erstelle ein DataPoint
                    if len(tmax_data) == len(tmin_data) and len(tmax_data) > 0:
                        data_point = DataPoint(date=current_date, tmax=tmax_data, tmin=tmin_data, station=station_id)
                        print(data_point)
                        tmax_data = []
                        tmin_data = []

    else:
        print(f"Fehler beim Herunterladen: HTTP {response.status_code}")



# Beispielaufruf
download_and_create_datapoints("ACW00011604")
