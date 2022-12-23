import os
import requests

from flask import Flask, render_template, request

REST_URL = os.environ.get ("REST_URL", "http://localhost/")

app = Flask(__name__)

@app.route("/")
def gspc_home():
    return render_template('index.html.j2')

def render_search_table(q=None):
    people_items = requests.get(REST_URL).json().get("_items")
    if q:
        people_items = [i for i in people_items \
            if q.lower() in i.get("firstname").lower() \
            or q.lower() in i.get("lastname").lower()]
    return render_template("search_table.html.j2", people_items=people_items)

@app.route("/people", methods=["GET", "POST"])
def gspc_people():
    if request.method == "POST":
        firstname = request.values.get("firstname")
        lastname = request.values.get("lastname")
        if firstname and lastname:
            requests.post(REST_URL, json={"firstname": firstname, "lastname": lastname}) 
    search_table = render_search_table()
    return render_template("people.html.j2", search_table=search_table)

@app.route("/search", methods=["GET"]) 
def startup_search():
    q = request.values.get("q")
    search_table = render_search_table(q=q)
    return render_template("search.html.j2", search_table=search_table, q=q)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
