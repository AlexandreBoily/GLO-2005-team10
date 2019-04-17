import mysql.connector

class updater:

    @classmethod
    def __update(cls, cursor, STMT, tuple, id):
        try:
            cursor.execute(STMT, tuple)
            return {"error": False,
                    "id": id}
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return {"error": True,
                    "msg": e.msg,
                    "no": e.errno}

    @classmethod
    def updateGame(cls, cursor, game):
        updateSTMT = "UPDATE GAMES SET game_name = %s WHERE id = %s "
        tuple = (game["game_name"], game["id"])
        return cls.__update(cursor, updateSTMT, tuple, game["id"])

    @classmethod
    def updateTeam(cls, cursor, team):
        updateSTMT = "UPDATE TEAMS SET name = %s WHERE id = %s"
        tuple = (team["name"], team["id"])
        return cls.__update(cursor, updateSTMT, tuple, team["id"])

    @classmethod
    def updatePlayer(cls, cursor, player):
        updateSTMT = "UPDATE PLAYERS SET first_name = %s," \
                     "last_name = %s," \
                     "alias = %s," \
                     "nationality = %s WHERE id = %s"
        tuple = (player["first_name"], player["last_name"], player["alias"], player['nationality'], player["id"])
        return cls.__update(cursor, updateSTMT, tuple, player["id"])

    @classmethod
    def updateOrganization(cls, cursor, org):
        updateSTMT = "UPDATE ORGANIZATION SET name = %s WHERE id = %s"
        tuple = (org["name"], org["id"])
        return cls.__update(cursor, updateSTMT, tuple, org["id"])

    @classmethod
    def updateLeague(cls, cursor, league):
        updateSTMT = "UPDATE LEAGUES SET name = %s,"\
                     "max_no_teams = %s" \
                     "description = %s" \
                     "region = %s" \
                     "prize_pool = %s" \
                     "online = %s WHERE shorthand = %s "
        tuple = (league["name"],
                 league["max_no_teams"],
                 league["description"],
                 league["region"],
                 league["prize_pool"],
                 league["online"],
                 league["shorthand"]
                 )

        return cls.__update(cursor, updateSTMT, tuple, league["shorthand"])


    @classmethod
    def updateRules(cls, cursor, rule):
        updateSTMT = "UPDATE RULES SET name = %s," \
                     "description = %s," \
                     "no_teams_per_match = %s," \
                     "no_players_per_teams = %s WHERE id = %s"
        tuple = (rule["name"], rule["description"], rule["no_teams_per_match"], rule["no_players_per_team"], rule["id"])
        return cls.__update(cursor, updateSTMT, tuple, rule["id"])