import logging

from api import api
from db import db
from config import app, create_config
from controllers import *
from models.db import ExampleModel

logger = logging.getLogger(__name__)
app.logger = logger

with app.app_context():
    app.logger.info("Starting API via gunicorn...")
    
    custom_config = create_config()
    app.config.update(custom_config)

    api.init_app(app)
    db.init_app(app)

    if app.config['TESTING']:
        db.create_all()
        db.session.add_all([ExampleModel(name="Batman"), ExampleModel(name="Superman"), ExampleModel(name="Spiderman")])
        db.session.commit()

    if __name__ == '__main__':
        ## Load temp data to speed up testing
        app.logger.info("Starting api locally...")
        app.run(debug=False, port=5000)
