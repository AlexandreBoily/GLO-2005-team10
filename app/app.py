#!/usr/bin/env python

from flask import Flask, render_template, request
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
    return render_template('list.html', items=games, pageName='Games')


@application.route("/leagues", methods=["GET"])
def leagues():
    global db
    games = db.getAll("LEAGUES")
    return render_template('list.html', items=games, pageName='Leagues')


@application.route("/players", methods=["GET"])
def players():
    global db
    games = db.getAll("PLAYERS")
    return render_template('list.html', items=games, pageName='Players')


@application.route("/teams", methods=["GET"])
def teams():
    global db
    games = db.getAll("TEAMS")
    return render_template('list.html', items=games, pageName='Teams')


@application.route("/game/<id>", methods=["GET"])
def game(id):
    global db
    return render_template('game.html', id=id)


@application.route("/league/<id>", methods=["GET"])
def league(id):
    global db
    return render_template('league.html', id=id)


@application.route("/player/<id>", methods=["GET"])
def player(id):
    global db
    return render_template('player.html', id=id)


@application.route("/team/<id>", methods=["GET"])
def team(id):
    global db
    return render_template('team.html', id=id)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)
