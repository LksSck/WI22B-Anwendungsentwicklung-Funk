class Station:
    def __init__(self, id: int, name: str, latitude: float, longitude: float):
        """
        Erstellt eine Wetterstation.

        :param id: Die eindeutige ID der Station (int).
        :param name: Der Name der Station (str).
        :param latitude: Die geografische Breite der Station (float).
        :param longitude: Die geografische Länge der Station (float).
        :param data: Eine Liste der Daten, die für diese Station gespeichert wurden (z. B. Wetterdaten).
        """
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """
        Repräsentation der Station als String.

        :return: String-Repräsentation der Station.
        """
        return f"Station(id={self.id}, name='{self.name}', latitude={self.latitude}, longitude={self.longitude})"
