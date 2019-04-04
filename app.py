from flask import Flask
application = Flask("my_application")

@application.route("/", methods=["GET","POST"])
def index():

    return "Hello World"

if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=8080)
