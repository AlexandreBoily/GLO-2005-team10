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
<<<<<<< HEAD
    games = db.getAll("GAMES")
    return render_template('list.html', items=games, pageName='Games')
=======
    return render_template('list.html', items=None, pageName='Games')
>>>>>>> c0b18f800949819750839009927d26be99db8953


@application.route("/leagues", methods=["GET"])
def leagues():
    global db
<<<<<<< HEAD
    games = db.getAll("LEAGUES")
    return render_template('list.html', items=games, pageName='Leagues')
=======
    return render_template('list.html', items=None, pageName='Leagues')
>>>>>>> c0b18f800949819750839009927d26be99db8953


@application.route("/players", methods=["GET"])
def players():
    global db
<<<<<<< HEAD
    games = db.getAll("PLAYERS")
    return render_template('list.html', items=games, pageName='Players')
=======
    return render_template('list.html', items=None, pageName='Players')
>>>>>>> c0b18f800949819750839009927d26be99db8953


@application.route("/teams", methods=["GET"])
def teams():
    global db
<<<<<<< HEAD
    games = db.getAll("TEAMS")
    return render_template('list.html', items=games, pageName='Teams')
=======
    return render_template('list.html', items=None, pageName='Teams')
>>>>>>> c0b18f800949819750839009927d26be99db8953


@application.route("/game/<id>", methods=["GET"])
def game(id):
    global db
    game = db.getGameByID(id)
    return render_template('game.html', game=game)


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
