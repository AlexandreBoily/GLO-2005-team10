#!/usr/bin/env python

from flask import Flask, render_template
from MySQLdb import MySQLRepository
application = Flask(__name__)

@application.route("/", methods=["GET","POST"])
def index():

    db = MySQLRepository()
    games = db.getGames()
    return render_template('index.html', games=games)

    # return "Hello World test"
if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)
