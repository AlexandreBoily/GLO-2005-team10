from flask import Flask, render_template
from MySQLdb import MySQLRepository
application = Flask("my_application")

@application.route("/", methods=["GET","POST"])
def index():

    # db = MySQLRepository()
    # plants = db.get_mushrooms()
    # return render_template('index.html', plants = plants)

    return "Hello World"
if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080)
