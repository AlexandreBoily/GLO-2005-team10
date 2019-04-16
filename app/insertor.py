import MySQLdb

class insertor:

    @classmethod
    def createNewGame(cls, cursor, game):
        insertSTMT = "INSERT INTO GAMES (game_name) VALUES (%s)"

        try:
            cursor.execute(insertSTMT, (game["game_name"],))
            cursor.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            cursor.rollback()


    @classmethod
    def createNewTeam(cls, cursor, game):
        return ""

