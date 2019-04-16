#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for
from MySQLdb import MySQLRepository


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
    game = db.getGameByID(league['game_id'])
    return render_template('league.html', league=league, game=game)


@application.route("/player/<id>", methods=["GET"])
def player(id):
    global db
    player = db.getPlayerByID(id)
    return render_template('player.html', player=player)


@application.route("/team/<id>", methods=["GET"])
def team(id):
    global db
    return render_template('team.html', id=id)

@application.route("/organization/<id>", methods=["GET"])
def organization(id):
    global db
    organization = db.getOrganizationByID(id)
    return render_template('organization.html', organization=organization)

@application.route("/create/<type>", methods=["GET", "POST"])
def create(type):
    global db
    if request.method == "POST":
        # access form data with request.form, ie: request.form['alias']
        # create new game then redirect to that game's page using it's id (instead of id=0)
        return redirect(url_for('team', id=request.form['first-name']))
    type = type[:-1]
    return render_template('create-form.html', type=type)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)
