from flask import Flask, render_template, request, redirect, url_for
from database import init_app, db
from models import User
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize app and database
init_app(app)

# Set up migrations
migrate = Migrate(app, db)

@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.name = request.form["name"]
        user.email = request.form["email"]
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

