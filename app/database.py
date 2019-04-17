#!/usr/bin/env python
from mysql.connector import connect
import mysql.connector
from selector import selector
from insertor import insertor
from updater import updater
from deletor import deletor

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

    def __commit(self, returned):
        if returned["error"]:
            return returned
        else:
            try:
                self.connector.commit()
                return returned
            except mysql.connector.Error as e:
                self.connector.rollback()
                return {"error": True,
                        "msg": e.msg,
                        "no": e.errno}

    def getAll(self, table_name):
        self.__verify_connection()
        return selector.getAll(self.connector.cursor(), table_name)

    def getAllNationalities(self):
        self.__verify_connection()
        return selector.getAllNationalities(self.connector.cursor())

    def getGameByID(self, id):
        self.__verify_connection()
        game = selector.getGameByID(self.connector.cursor(), id)
        return game

    def getLeagueByID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()
        return selector.getLeagueByID(cursor, id)

    def getTeamByID(self, id):
        self.__verify_connection()
        cursor = self.connector.cursor()
        return selector.getTeamByID(cursor, id)

    def getPlayerByID(self, id):
        self.__verify_connection()
        return selector.getPlayerByID(self.connector.cursor(), id)

    def getOrganizationByID(self, id):
        self.__verify_connection()
        return selector.getOrganizationByID(self.connector.cursor(), id)

    def createNewGame(self, game):
        self.__verify_connection()
        return self.__commit(insertor.createNewGame(self.connector.cursor(), game))

    def createNewLeague(self, league):
        self.__verify_connection()
        return self.__commit(insertor.createNewLeague(self.connector.cursor(), league))

    def createNewPlayer(self, player):
        self.__verify_connection()
        return self.__commit(insertor.createNewPlayer(self.connector.cursor(), player))

    def createNewTeam(self, team):
        self.__verify_connection()
        return self.__commit(insertor.createNewTeam(self.connector.cursor(), team))

    def createNewOrganization(self, organization):
        self.__verify_connection()
        return self.__commit(insertor.createNewOrganization(self.connector.cursor(), organization))

    def update(self, table, object):
        self.__verify_connection()
        return self.__commit(updater.update_prep(self.connector.cursor(), table, object))
    
    def delete(self, table, id):
        self.__verify_connection()
        return self.__commit(deletor.delete_prep(self.connector.cursor(), table, id))
