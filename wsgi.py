from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! - My Name is Ryan Loiselle, and Lisa is sitting next to me and we are doing the HelloWold demo on OpenShift"

if __name__ == "__main__":
    application.run()
