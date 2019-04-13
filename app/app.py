#!/usr/bin/env python

from flask import Flask, render_template
from MySQLdb import MySQLRepository
application = Flask(__name__)


db = MySQLRepository()


@application.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html')


@application.route("/games", methods=["GET"])
def games():
    global db
    games = db.getAllGames()
    return render_template('list.html', items=games, pageName='Games')


@application.route("/leagues", methods=["GET"])
def leagues():
    global db
    games = db.getGames()
    return render_template('list.html', items=games, pageName='Leagues')


@application.route("/players", methods=["GET"])
def players():
    global db
    games = db.getGames()
    return render_template('list.html', items=games, pageName='Players')


@application.route("/teams", methods=["GET"])
def teams():
    global db
    games = db.getGames()
    return render_template('list.html', items=games, pageName='Teams')


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)
