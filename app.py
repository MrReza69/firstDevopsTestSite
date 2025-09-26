from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
Bootstrap(app)

# مدل ساده دیتابیس
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # دیتابیس اولیه ساخته میشه
        if not User.query.first():
            db.session.add(User(name="Ali"))
            db.session.add(User(name="Sara"))
            db.session.commit()
    app.run(host="0.0.0.0", port=5000)

