import mysql.connector

class linker:

    @classmethod
    def __link(cls, cursor, STMT, tuple):
        try:
            cursor.execute(STMT, tuple)
            return {"error": False,
                    "id": (tuple[0], tuple[1])}
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return {"error": True,
                    "msg": e.msg,
                    "no": e.errno}
    @classmethod
    def linkPlayerTeams(cls, cursor, player_id, team_id, **kwargs):
        tuple = (player_id, team_id)
        if not kwargs:
            insertSTMT = "INSERT INTO PLAYERS_TEAMS (player_id, team_id) VALUES (%s,%s)"
        else:
            if "start" in kwargs:
                insertSTMT = "INSERT INTO PLAYERS_TEAMS (player_id, team_id, start) VALUES (%s,%s,%s)"
                tuple = tuple + (kwargs["start"],)
            elif "end" in kwargs:
                insertSTMT = "INSERT INTO PLAYERS_TEAMS (player_id, team_id, end) VALUES (%s,%s,%s)"
                tuple = tuple + (kwargs["end"],)
            elif "start" in kwargs and "end" in kwargs:
                insertSTMT = "INSERT INTO PLAYERS_TEAMS (player_id, team_id, start, end) VALUES (%s,%s,%s,%s)"

        return cls.__link(cursor, insertSTMT, tuple)

    @classmethod
    def linkTeamLeague(cls, cursor, team_id, league_id, **kwargs):
        if "result" in kwargs:
            insertSTMT = "INSERT INTO TEAMS_LEAGUES (team_id, league_id, result) VALUES (%s, %s, %s)"
            tuple = (team_id,league_id,kwargs["result"])
        else:
            insertSTMT = "INSERT INTO TEAMS_LEAGUES (team_id, league_id) VALUES (%s, %s)"
            tuple = (team_id, league_id)

        return cls.__link(cursor, insertSTMT, tuple)
