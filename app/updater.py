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
    def update_prep(cls, cursor, table, object):
        switch = {
            "GAMES": {"STMT": "UPDATE GAMES SET game_name = %s WHERE id = %s",
                      "tuple": (object["game_name"], object["id"]),
                      "id": object["id"]},
            "TEAMS": {"STMT": "UPDATE TEAMS SET name = %s WHERE id = %s",
                      "tuple": (object["name"], object["id"]),
                      "id": object["id"]},
            "PLAYERS": {"STMT": "UPDATE PLAYERS SET first_name = %s, last_name = %s, alias = %s, nationality = %s WHERE id = %s",
                      "tuple": (object["first_name"], object["last_name"], object["alias"], object['nationality'], object["id"]),
                      "id": object["id"]},
            "ORGANIZATION": {"STMT": "UPDATE ORGANIZATION SET name = %s WHERE id = %s",
                      "tuple": (object["name"], object["id"]),
                      "id": object["id"]},
            "LEAGUES": {"STMT": "UPDATE LEAGUES SET name = %s, max_no_teams = %s, description = %s, region = %s, prize_pool = %s, online = %s WHERE shorthand = %s ",
                      "tuple": (object["name"],
                             object["max_no_teams"],
                             object["description"],
                             object["region"],
                             object["prize_pool"],
                             object["online"],
                             object["shorthand"]
                             ),
                      "id": object["shorthand"]},
            "RULES": {"STMT": "UPDATE RULES SET name = %s, description = %s, no_teams_per_match = %s, no_players_per_teams = %s WHERE id = %s",
                      "tuple": (object["name"], object["description"], object["no_teams_per_match"], object["no_players_per_team"], object["id"]),
                      "id": object["id"]},
        }

        result = switch[table]
        return cls.__update(cursor, result["STMT"], result["tuple"], result["id"])