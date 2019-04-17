import mysql.connector

class insertor:

    @classmethod
    def __insert(cls, cursor, STMT, tuple):
        try:
            cursor.execute(STMT, tuple)
            return {"error": False,
                    "id": cursor.lastrowid}
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return {"error": True,
                    "msg": e.msg,
                    "no": e.errno}

    @staticmethod
    def __returnID(cursor):
        stmt = "SELECT LAST_INSERT_ID();"
        cursor.execute(stmt)
        return cursor.fetchone()[0]

    @classmethod
    def createNewGame(cls, cursor, game):
        insertSTMT = "INSERT INTO GAMES (game_name) VALUES (%s)"
        tuple = (game["game_name"],)
        return cls.__insert(cursor, insertSTMT, tuple)


    @classmethod
    def createNewTeam(cls, cursor, team):
        insertSTMT = "INSERT INTO TEAMS (name) VALUES (%s)"
        tuple = (team["name"],)
        return cls.__insert(cursor, insertSTMT, tuple)

    @classmethod
    def createNewPlayer(cls, cursor, player):
        insertSTMT = "INSERT INTO PLAYER (first_name, last_name, alias) VALUES (%s, %s, %s)"
        tuple = (player["first_name"], player["last_name"], player["alias"])
        return cls.__insert(cursor, insertSTMT, tuple)

    @classmethod
    def createNewOrganization(cls,cursor, org):
        insertSTMT = "INSERT INTO ORGANIZATION (name) VALUES (%s)"
        tuple = (org["name"],)
        return cls.__insert(cursor, insertSTMT, tuple)

    @classmethod
    def createNewLeague(cls, cursor, league):
        insertSTMT = "INSERT INTO LEAGUES (shorthand, name, max_no_teams, description, region, prize_pool, online) VALUES" \
                     "(%s,%s,%s,%s,%s,%s)"
        tuple = (league["shorthand"],
                 league["name"],
                 league["max_no_teams"],
                 league["description"],
                 league["region"],
                 league["prize_pool"],
                 league["online"])

        returned = cls.__insert(cursor, insertSTMT, tuple)
        if not returned["error"]:
            returned["id"] = league["shorthand"]
            return returned
        else:
            return returned

    @classmethod
    def createNewRules(cls, cursor, rule):
        insertSTMT = "INSERT INTO RULES (name, description, no_teams_per_match, no_players_per_teams) VALUES (%s, %s, %s)"
        tuple = (rule["name"], rule["description"], rule["no_teams_per_match"], rule["no_players, per_team"])
        return cls.__insert(cursor, insertSTMT, tuple)

