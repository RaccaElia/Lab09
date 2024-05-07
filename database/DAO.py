from database.DB_connect import DBConnect
from model.volo import Volo

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ID, AIRPORT, IATA_CODE
                    from extflightdelays.airports"""

        cursor.execute(query)

        for row in cursor:
            result.append([row["ID"], row["AIRPORT"], row["IATA_CODE"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getFlightsDistance(distanza):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, avg(f.DISTANCE) as media
                    from extflightdelays.flights f 
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                    having avg(f.DISTANCE)>%s"""

        cursor.execute(query, (distanza, ))

        for row in cursor:
            result.append(Volo(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["media"]))

        cursor.close()
        conn.close()
        return result