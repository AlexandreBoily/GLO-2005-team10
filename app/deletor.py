import mysql.connector

class deletor:

    @classmethod
    def __delete(cls, cursor, STMT, tuple):
        try:
            cursor.execute(STMT, tuple)
            return {"error": False,
                    "id": cursor.lastrowid}
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
        deleteSTMT = "DELETE FROM TEAMS WHERE name=%s"
        tuple = (team["name"],)
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deletePlayer(cls, cursor, player):
        deleteSTMT = "DELETE FROM PLAYERS WHERE id=%s"
        tuple = (player["id"])
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deleteOrganization(cls,cursor, org):
        deleteSTMT = "DELETE FROM ORGANIZATION WHERE name=%s"
        tuple = (org["name"],)
        return cls.__delete(cursor, deleteSTMT, tuple)

    @classmethod
    def deleteLeague(cls, cursor, league):
        deleteSTMT = "DELETE FROM LEAGUES WHERE shorthand=%s"
        tuple = (league["shorthand"])

        returned = cls.__delete(cursor, deleteSTMT, tuple)
        if not returned["error"]:
            return {
                "error": False,
                "id": league["shorthand"]
            }
        else:
            return returned

    @classmethod
    def deleteRules(cls, cursor, rule):
        deleteSTMT = "DELETE FROM RULES WHERE id=%s"
        tuple = (rule["id"])
        return cls.__delete(cursor, deleteSTMT, tuple)

