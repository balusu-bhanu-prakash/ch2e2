from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! This is deployed on AWS Elastic Beanstalk."

if __name__ == "__main__":
    app.run(debug=True)