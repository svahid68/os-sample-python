from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! - My Name is Ryan Loiselle, this is the Tuesday Tech Talk about OpenShift and DevOps"

if __name__ == "__main__":
    application.run()
