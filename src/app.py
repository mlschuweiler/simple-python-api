import logging
from api import api
from db import db
from config import app
from controllers import *
from models.db import ExampleModel

logger = logging.getLogger(__name__)
app.logger = logger

with app.app_context():
    app.logger.info("Starting API via gunicorn...")
    api.init_app(app)
    db.init_app(app)
    db.create_all()

    ## Load temp data to speed up testing
    db.session.add_all([ExampleModel(name="Batman"), ExampleModel(name="Superman"), ExampleModel(name="Spiderman")])
    db.session.commit()

    if __name__ == '__main__':
        app.logger.info("Starting api locally...")
        app.run(debug=True, port=5000)
