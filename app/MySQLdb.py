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

    def getAllGames(self):
        self.__verify_connection()
        cursor = self.connector.cursor()
        getAllGamesSTMT = "SELECT * FROM GAMES"
        cursor.execute(getAllGamesSTMT)
        games = [(game[0], game[1]) for game in cursor]
        return games

    def getGameByID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()

        #Get game name and id
        getGameByIDSTMT = "SELECT * FROM GAMES g WHERE g.id = %s "
        cursor.execute(getGameByIDSTMT, (id,))
        tmp = cursor.fetchone()
        game = {
            "id":  tmp[0],
            "game_name": tmp[1]
        }

        #Game list of leagues
        getGamesLeaguesSTMT = "SELECT shorthand, name FROM LEAGUES l WHERE l.game_id = %s"
        cursor.execute(getGamesLeaguesSTMT, (game['id'],))
        leagues = [(league[0], league[1]) for league in cursor]
        game["leagues"] = leagues

        return game

