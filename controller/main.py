#from model.passive_teacher import passive_teacher
from flask import Flask, request, render_template, redirect
from markupsafe import escape  # esto sirve para evitar inyecciones
from werkzeug.middleware.proxy_fix import ProxyFix
import os
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

    # for folder in os.listdir(BASE_DIR):
    #     folder_path = os.path.join(BASE_DIR, folder)

    #     if os.path.isdir(folder_path):
    #         files = [f for f in os.listdir(folder_path) 
    #                  if f.endswith(".pdf") and not f.startswith(".")]
            
    #         structure[folder] = files

    # print("holaaa")
    directorio = requests.get("http://files_container/")
    # print(directorio)
    # sys.stdout.flush()

    print(directorio.status_code)
    print(directorio.headers)
    print(directorio.text)

    sys.stdout.flush()

    return render_template("biblioteca.html", structure=structure)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)   