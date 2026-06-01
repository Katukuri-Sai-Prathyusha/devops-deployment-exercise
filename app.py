from flask import Flask



app = Flask(__name__)



@app.route("/")

def home():

    return """

    <h1>DevOps CI/CD Deployment Exercise</h1>

    <h2>Version: v1.2 - Auto deployed by GitHub Actions</h2>

    <p>Status: Running successfully</p>

    """



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
