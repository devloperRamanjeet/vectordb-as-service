from database.db import db

class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    task_arn = db.Column(db.String)
    port = db.Column(db.Integer)
    status = db.Column(db.String)
