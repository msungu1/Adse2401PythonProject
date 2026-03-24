from flask import Flask, render_template
from my_flask_app import register # your form file

app = Flask(__name__)
app.secret_key = "mysecretkey"   # required for Flask-WTF


@app.route("/register", methods=["GET", "POST"])
def register():
    form = register()
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)