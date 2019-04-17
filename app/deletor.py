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
    def delete_prep(cls, cursor, table, id):
        switch = {
            "GAMES": "DELETE FROM GAMES WHERE id = %s",
            "TEAMS": "DELETE FROM TEAMS WHERE id = %s",
            "PLAYERS": "DELETE FROM PLAYERS WHERE id = %s",
            "ORGANIZATION": "DELETE FROM ORGANIZATION WHERE id = %s",
            "LEAGUES": "DELETE FROM LEAGUES WHERE shorthand = %s",
            "RULES": "DELETE FROM RULES WHERE id=%s"
        }
        return cls.__delete(cursor, switch[table], (id,))

