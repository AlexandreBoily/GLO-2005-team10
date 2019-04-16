class selector:

    @staticmethod
    def __prepareGetAllSTMT(table_name):
        switch = {
            "LEAGUES": ("shorthand", "name"),
            "GAMES": ("id", "game_name"),
            "PLAYERS": ("id", "alias"),
            "TEAMS": ("id", "name")
        }
        fields = switch.get(table_name, "error")
        return "SELECT {}, {} FROM {}".format(fields[0], fields[1], table_name)

    @classmethod
    def getAll(cls, cursor, table_name):
        cursor.execute(cls.__prepareGetAllSTMT(table_name))
        games = [(game[0], game[1].replace('"', '')) for game in cursor]
        return games

    @classmethod
    def getGameByID(cls, cursor, id):

        # Get game name and id
        getGameByIDSTMT = "SELECT * FROM GAMES g WHERE g.id = %s "
        cursor.execute(getGameByIDSTMT, (id,))
        tmp = cursor.fetchone()
        game = {
            "id": tmp[0],
            "game_name": tmp[1].replace('"', '')
        }

        # Game list of leagues
        getGamesLeaguesSTMT = "SELECT shorthand, name FROM LEAGUES l WHERE l.game_id = %s"
        cursor.execute(getGamesLeaguesSTMT, (game['id'],))
        leagues = [{'shorthand': league[0], "name": league[1]} for league in cursor]
        game["leagues"] = leagues

        return game

    @classmethod
    def getLeagueByID(cls, cursor, id):

        getLeagueByIDSTMT = "SELECT * FROM LEAGUES l where l.shorthand = %s"
        getRuleSTMT = "SELECT * FROM RULES WHERE id = %s"
        getTeamsSTMT = "SELECT t.id, t.name, l.result FROM TEAMS t INNER JOIN TEAMS_LEAGUES l "

        # Get game ID and shorthand
        cursor.execute(getLeagueByIDSTMT, (id,))
        tmp = cursor.fetchone()
        league = {
            "name": tmp[1],
            "max_no_teams": tmp[2],
            "description": tmp[3],
            "region": tmp[4],
            "prize_pool": tmp[5],
            "online": tmp[6],
            "game_id": tmp[7]
        }

        # Get rules
        cursor.execute(getRuleSTMT, (tmp[8],))
        tmp = cursor.fetchone()
        rule = {
            "id": tmp[0],
            "name": tmp[1],
            "max_no_teams": tmp[2],
            "no_teams_per_match": tmp[3],
            "no_players_per_teams": tmp[4]
        }
        league["rule"] = rule

        # Get teams participating in this league
        cursor.execute(getTeamsSTMT, (id,))
        teams = [{"id": team[0], "name": team[1], "result": team[2]} for team in cursor]
        league["teams"] = teams

        return league

    @classmethod
    def getTeamByID(cls, cursor, id):

        getTeamByIDSTMT = "SELECT id, name FROM TEAMS WHERE id = %s"
        getOrganizationSTMT = "SELECT o.name FROM ORGANIZATION o INNER JOIN TEAMS t on t.organization_id = o.id"
        getLeaguesSTMT = "SELECT t.shorthand, t.name, l.result FROM LEAGUES t INNER JOIN TEAMS_LEAGUES l ON l.league_id = t.shorthand WHERE l.team_id = %s"
        getPlayersSTMT = "SELECT p.id, p.alias, t.start, t.end FROM PLAYERS p INNER JOIN PLAYER_TEAMS t ON t.player_id = p.id WHERE t.team_id = %s"

        #Get team id and name
        cursor.execute(getTeamByIDSTMT, (id,))
        tmp = cursor.fetchone()
        team = {
            "id": tmp[0],
            "name": tmp[1]
        }

        #Get org name
        cursor.execute(getOrganizationSTMT)
        tmp = cursor.fetchone()
        team["org_name"] = tmp[0]

        #Get Leagues in which the team participates
        cursor.execute(getLeaguesSTMT, (id,))
        leagues = [{"shorthand": league[0], "name": league[1], "result": league[2]} for league in cursor]
        team["leagues"] = leagues

        #Get Players
        cursor.execute(getPlayersSTMT, (id,))
        players = [{"id": player[0], "alias": player[1], "start": player[2], "end": player[3]} for player in cursor]
        team["players"] = players

        return team