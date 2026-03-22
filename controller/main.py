#from model.passive_teacher import passive_teacher
from flask import Flask, request, render_template
from markupsafe import escape  # esto sirve para evitar inyecciones



app = Flask(__name__, template_folder="../view")

@app.route("/")
@app.route("/<name>")
def welcome(name = None):
    #name = request.args.get("")
    return render_template('/index.html', user= name)

@app.route("/sign-in")
def sign_in():
    pass

@app.route("/directory")
def directory():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)   