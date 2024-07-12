from http import HTTPStatus
from flask_restx import Resource
from flask import current_app as app

from api import api

health_ns = api.namespace('health', description='API Health Endpoint')

parser = api.parser()
# parser.add_argument('HEADER_NAME', location='headers', type=str)

@health_ns.route("/health")
class Health(Resource):
    
    @health_ns.doc("enternal:getHealth")
    @health_ns.expect(parser)
    @health_ns.response(HTTPStatus.OK, "Success")
    # Add more response types like this for HTTPStatus.* (INTERNAL_SERVER_ERROR, etc)
    def get(self):
        app.logger.info("Returning /health:")
        return {
            "status": "ok"
        }, HTTPStatus.OK
