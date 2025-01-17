class DataPoint:
    def __init__(self, date: int, station=None):
        """
        Erstellt einen Datenpunkt mit Monat, Temperaturdaten und einer zugehörigen Station.

        :param date: Jahr+Monat im Format YYYYMM (z. B. 202401).
        :param station: Die Station (Instanz der Klasse Station), der dieser Datenpunkt zugeordnet ist.
        """

        self.date = date
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
        station_name = self.station.name if self.station else "None"
        return f"DataPoint(date={year}-{month:02d}, station='{station_name}')"
