#!/usr/bin/env python
from mysql.connector import connect

class MySQLRepository:
    MYSQL_URI = "db"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = None
    DATABASE_NAME = "PlantsDatabase"
    DATABASE_CONFIG_FILE = "./databaseconfig/plants.sql"

    def __init__(self):
        self.connector = None
        try:
            self.__connect()
        except Exception as exception:
            print(exception)

        #self.__configure()

    def __connect(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD,
                                 database=self.DATABASE_NAME)

    def __configure(self):
        self.__verify_connection()
        cursor = self.connector.cursor()
        configFile = open(self.DATABASE_CONFIG_FILE, "r")
        commands = configFile.read().split(";")
        for c in commands:
            cursor.execute(c)
        configFile.close()

    def __verify_connection(self):
        if self.connector is None:
            self.__connect()

    def get_mushrooms(self):
        self.__verify_connection()
        select_query = "SELECT DISTINCT common_name FROM plants"
        cursor = self.connector.cursor()
        cursor.execute(select_query)

        return [{plants[0]} for plants in cursor]