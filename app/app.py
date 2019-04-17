#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for
from database import MySQLRepository


application = Flask(__name__)


db = MySQLRepository()


@application.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html')


@application.route("/games", methods=["GET"])
def games():
    global db
    games = db.getAll("GAMES")
    return render_template('list.html', items=games, pageName='Games', itemType='game')

@application.route("/leagues", methods=["GET"])
def leagues():
    global db
    leagues = db.getAll("LEAGUES")
    return render_template('list.html', items=leagues, pageName='Leagues', itemType='league')

@application.route("/players", methods=["GET"])
def players():
    global db
    players = db.getAll("PLAYERS")
    return render_template('list.html', items=players, pageName='Players', itemType='player')


@application.route("/teams", methods=["GET"])
def teams():
    global db
    teams = db.getAll("TEAMS")
    return render_template('list.html', items=teams, pageName='Teams', itemType='team')

@application.route("/organizations", methods=["GET"])
def organizations():
    global db
    organizations = db.getAll("ORGANIZATION")
    return render_template('list.html', items=organizations, pageName='Organizations', itemType='organization')


@application.route("/game/<id>", methods=["GET"])
def game(id):
    global db
    game = db.getGameByID(id)
    return render_template('game.html', game=game)


@application.route("/league/<id>", methods=["GET"])
def league(id):
    global db
    league = db.getLeagueByID(id)
    if league['game_id'] is not None:
        game = db.getGameByID(league['game_id'])
    else:
        game = None
    return render_template('league.html', league=league, game=game)


@application.route("/player/<id>", methods=["GET"])
def player(id):
    global db
    player = db.getPlayerByID(id)
    return render_template('player.html', player=player)


@application.route("/team/<id>", methods=["GET"])
def team(id):
    global db
    team = db.getTeamByID(id)
    return render_template('team.html', team=team)

@application.route("/organization/<id>", methods=["GET"])
def organization(id):
    global db
    organization = db.getOrganizationByID(id)
    return render_template('organization.html', organization=organization)

@application.route("/create/<type>", methods=["GET", "POST"])
def create(type):
    global db
    if request.method == "POST":
        if type == "Games":
            id = db.createNewGame({
                "game_name": request.form["name"],
            })
            if id["error"]:
                return id["msg"]
            else:
                return redirect(url_for('game', id=id["id"]))
        elif type == "Leagues":
            id = db.createNewLeague({
                "name": request.form["name"],
                "shorthand": request.form["shorthand"],
                "max_no_teams": request.form["max-no-teams"],
                "description": request.form["description"],
                "region": request.form["region"],
                "prize_pool": request.form["prize-pool"],
                "online": request.form["online"],
            })
            if id["error"]:
                return id["msg"]
            else:
                return redirect(url_for('league', id=id["id"]))
        elif type == "Players":
            id = db.createNewPlayer({
                "first_name": request.form['first-name'],
                "last_name": request.form['last-name'],
                "alias": request.form['alias'],
            })
            if id["error"]:
                return id["msg"]
            else:
                return redirect(url_for('player', id=id["id"]))
        elif type == "Teams":
            id = db.createNewTeam({
                "name": request.form['name'],
            })
            if id["error"]:
                return id["msg"]
            else:
                return redirect(url_for('team', id=id["id"]))
    type = type[:-1]
    return render_template('create-form.html', type=type)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)
