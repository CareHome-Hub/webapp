from flask import Flask, Response
from py2neo import Graph

g = Graph('bolt://localhost:7687')


app = Flask(__name__)


@app.route("/")
def hello():
    df = g.run(
        "MATCH (a :company) RETURN a.company_id as company_id, a.name as name, a.industry as industry  LIMIT 4").data()
    print("\n\nDF = {}s".format(df))
    return Response("Hi from your Flask app running in your Docker container! {}".format(df))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
