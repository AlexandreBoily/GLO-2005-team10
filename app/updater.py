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
                      "tuple": ("game_name", "id"),
                      "id": "id"},

            "TEAMS": {"STMT": "UPDATE TEAMS SET name = %s WHERE id = %s",
                      "tuple": ("name", "id"),
                      "id": "id"},

            "PLAYERS": {"STMT": "UPDATE PLAYERS SET first_name = %s, last_name = %s, alias = %s, nationality = %s WHERE id = %s",
                      "tuple": ("first_name", "last_name", "alias", 'nationality', "id"),
                      "id": "id"},

            "ORGANIZATION": {"STMT": "UPDATE ORGANIZATION SET name = %s WHERE id = %s",
                      "tuple": ("name", "id"),
                      "id": "id"},
            "LEAGUES": {"STMT": "UPDATE LEAGUES SET name = %s, max_no_teams = %s, description = %s, region = %s, prize_pool = %s, online = %s WHERE shorthand = %s ",
                      "tuple": ("name",
                                "max_no_teams",
                                "description",
                                "region",
                                "prize_pool",
                                 "online",
                                 "shorthand"
                                ),
                      "id": "shorthand"},
            "RULES": {"STMT": "UPDATE RULES SET name = %s, description = %s, no_teams_per_match = %s, no_players_per_teams = %s WHERE id = %s",
                      "tuple": ("name", "description", "no_teams_per_match", "no_players_per_team", "id"),
                      "id": "id"}
        }

        result = switch[table]
        return cls.__update(cursor, result["STMT"], (object[x] for x in result["tuple"]), object[result["id"]])