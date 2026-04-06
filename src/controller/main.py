#from model.passive_teacher import passive_teacher
from flask import Flask, request, render_template, redirect
from markupsafe import escape  # esto sirve para evitar inyecciones
from werkzeug.middleware.proxy_fix import ProxyFix
import requests
import sys

BASE_DIR = "files_container"

#hola
app = Flask(__name__, template_folder="../view")
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

@app.route("/")
@app.route("/<name>")
def welcome(name = None):
    #name = request.args.get("")
    return render_template('/index.html', user= name)

@app.route("/sign-in")
def sign_in():
    pass

@app.route("/biblioteca")
def biblioteca():
    structure = {}  #diccionario de la biblioteca

    directorio = requests.get("http://files_container/").json()
    print(type(directorio))

    for item in directorio:
        if item["type"] == "directory":
            sub_dir = item["name"]

            sub_dir_content = requests.get(f"http://files_container/{sub_dir}").json()
            files = [file["name"] for file in sub_dir_content 
                     if file["type"] == "file" and file["name"].endswith(".pdf")]
            
            structure[sub_dir]=files

    # sys.stdout.flush()

    print(structure)
    sys.stdout.flush()

    return render_template("biblioteca.html", structure=structure)


@app.route("/get_file/<folder>/<file>")
def get_file(folder, file):
    return redirect(f"/files_container/{folder}/{file}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)   