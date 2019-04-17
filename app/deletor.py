import mysql.connector

class deletor:

    @classmethod
    def __delete(cls, cursor, STMT, tuple):
        try:
            cursor.execute(STMT, tuple)
            return {"error": False}
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return {"error": True,
                    "msg": e.msg,
                    "no": e.errno}

    @classmethod
    def deleteGame(cls, cursor, game):
        deleteSTMT = "DELETE FROM GAMES WHERE id=%s"
        tuple = (game["id"],)
        return cls.__delete(cursor, deleteSTMT, tuple)


    @classmethod
    def deleteTeam(cls, cursor, team):
        deleteSTMT = "DELETE FROM TEAMS WHERE id=%s"
        tuple = (team["id"],)
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deletePlayer(cls, cursor, player):
        deleteSTMT = "DELETE FROM PLAYERS WHERE id=%s"
        tuple = (player["id"])
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deleteOrganization(cls,cursor, org):
        deleteSTMT = "DELETE FROM ORGANIZATION WHERE id=%s"
        tuple = (org["id"],)
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deleteLeague(cls, cursor, league):
        deleteSTMT = "DELETE FROM LEAGUES WHERE shorthand=%s"
        tuple = (league["shorthand"])
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deleteRules(cls, cursor, rule):
        deleteSTMT = "DELETE FROM RULES WHERE id=%s"
        tuple = (rule["id"])
        return cls.__delete(cursor, deleteSTMT, tuple)

