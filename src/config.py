import logging.config

from flask import Flask

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'json': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(funcName)s %(message)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        },
    },
    'handlers': {
        'json': {
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        '': {
            'handlers': ['json'],
            'level': logging.INFO
        }
    }
})

app = Flask(__name__)
app.config["EXAMPLE_CONFIG_KEY"] = "VALUE"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"