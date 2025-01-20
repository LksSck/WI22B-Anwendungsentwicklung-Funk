import mysql.connector
import station
import datapoint as dp

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()

stations = station.load_stations_from_url("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.csv")
# stations = [station.Station(id="ZI000067983", latitude=1, longitude=1)]
for station in stations:
    station_id = station.id

    cursor.execute(f"INSERT INTO Station(id, latitude, longitude) "
                   f"VALUES('{station_id}', '{station.latitude}', '{station.longitude}');")

    weather_data = dp.download_and_create_datapoints(station_id)
    for datapoint in weather_data:
        cursor.execute(f"INSERT INTO Datapoint (station_id, year, month, tmax, tmin) "
                       f"VALUES ('{datapoint.station}', '{str(datapoint.date)[:4]}', '{str(datapoint.date)[-2:]}', {datapoint.tmax}, {datapoint.tmin});")

cursor.execute("SELECT * FROM *;")
db_stations = cursor.fetchall()
connection.close()

print(db_stations)