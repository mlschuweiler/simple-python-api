from db import db

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(24), unique=True)

