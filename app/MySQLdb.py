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

    def __prepareGetAllSTMT(self, table_name):
        switch = {
            "LEAGUES": ("shorthand", "name"),
            "GAMES": ("id", "game_name"),
            "PLAYERS": ("id", "alias"),
            "TEAMS": ("id", "name")
        }
        fields = switch.get(table_name, "error")
        return (fields[0], fields[1], table_name)

    def getAll(self, table_name):
        self.__verify_connection()
        cursor = self.connector.cursor()
<<<<<<< HEAD
        cursor.execute("SELECT %s, %s FROM %s", self.__prepareGetAllSTMT(table_name))
        games = [(game[0], game[1]) for game in cursor]
=======
        getAllGamesSTMT = "SELECT * FROM GAMES"
        cursor.execute(getAllGamesSTMT)
        games = [(game[0], game[1].replace('"', '')) for game in cursor]
>>>>>>> c0b18f800949819750839009927d26be99db8953
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
            "game_name": tmp[1].replace('"', '')
        }

        #Game list of leagues
        getGamesLeaguesSTMT = "SELECT shorthand, name FROM LEAGUES l WHERE l.game_id = %s"
        cursor.execute(getGamesLeaguesSTMT, (game['id'],))
        leagues = [(league[0], league[1]) for league in cursor]
        game["leagues"] = leagues

        return game

