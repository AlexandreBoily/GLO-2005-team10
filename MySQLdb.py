#!/usr/bin/env python
from mysql.connector import connect

class MySQLRepository:
    MYSQL_URI = "db"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = None
    DATABASE_NAME = "EsportsWiki"
    DATABASE_CONFIG_FILE = "./databasedata/config_init.sql"

    def __init__(self):
        self.connector = None
        try:
            self.__connect()
        except Exception as exception:
            print(exception)

    def __connect(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD,
                                 database=self.DATABASE_NAME)

    def __verify_connection(self):
        if self.connector is None:
            self.__connect()

    def getGames(self):
        self.__verify_connection()
        cursor = self.connector.cursor()
        cursor.execute("SELECT game_name FROM GAMES")
        games =  [{'game_name': game[0]} for game in cursor]
        print(games)
        return games


