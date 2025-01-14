from db import db
from models.db import ExampleModel

def db_create_example_data():
    db.create_all()
    db.session.add_all([ExampleModel(name="Batman"), ExampleModel(name="Superman"), ExampleModel(name="Spiderman")])
    db.session.commit()
