#from model.passive_teacher import passive_teacher
from flask import Flask, request, render_template, redirect
from markupsafe import escape  # esto sirve para evitar inyecciones
from werkzeug.middleware.proxy_fix import ProxyFix



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

@app.route("/directory")
def directory():
    return redirect("/files_container/python/python_cs.pdf")


if __name__ == '__main__':
    print("hola")
    app.run(host='0.0.0.0', port=8080, debug=True)   