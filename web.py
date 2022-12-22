from flask import Flask, render_template, request
# import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

# @app.route("/", methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         firstname = request.values.get('firstname')
#         lastname = request.values.get('lastname')
#         requests.post(REST_URL, json={'firstname':firstname, 'lastname':lastname})
#     result = requests.get(REST_URL).json()
    # return render_template("index.html.j2", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
