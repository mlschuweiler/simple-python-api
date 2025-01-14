from http import HTTPStatus
from flask_restx import Resource
from config import app

from api import api

health_namespace = api.namespace('health', description='API Health Endpoint')

# parser = api.parser()
# parser.add_argument('HEADER_NAME', location='headers', type=str)

@health_namespace.route("/")
class Health(Resource):
    
    @health_namespace.doc("get_health")
    # @health_namespace.expect(parser)
    @health_namespace.response(HTTPStatus.OK, "Success")
    # Add more response types like this for HTTPStatus.* (INTERNAL_SERVER_ERROR, etc)
    def get(self):
        app.logger.info("Returning /health:")
        return {
            "status": "ok"
        }, HTTPStatus.OK
