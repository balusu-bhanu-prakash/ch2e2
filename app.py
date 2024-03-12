from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! This is deployed on AWS Elastic Beanstalk."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)  # Listen on all interfaces and port 8081
