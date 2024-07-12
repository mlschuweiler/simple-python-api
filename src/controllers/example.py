from http import HTTPStatus
from flask_restx import Resource
from flask import current_app as app
from app import db
from api import api

from models.db.example_models import ExampleModel
from models.json.example_schemas import example_schema, example_input_schema

example_namespace = api.namespace('examples', description='Example Endpoints')

parser = api.parser()
# parser.add_argument('HEADER_NAME', location='headers', type=str)

@example_namespace.route("/examples")
class ExampleListAPI(Resource):
    
    @example_namespace.doc("enternal:getExample")
    @example_namespace.expect(parser)
    @example_namespace.response(HTTPStatus.OK, "Success")
    # Add more response types like this for HTTPStatus.* (INTERNAL_SERVER_ERROR, etc)
    @example_namespace.marshal_list_with(example_schema)
    def get(self):
        # return ""
        return ExampleModel.query.all()
    
    @example_namespace.expect(example_input_schema)
    @example_namespace.marshal_with(example_schema)
    def post(self):
        example = ExampleModel(name=example_namespace.payload["name"])
        db.session.add(example)
        db.session.commit()
        return example, 201


@example_namespace.route("/examples/<int:id>")
class ExampleAPI(Resource):
    @example_namespace.marshal_with(example_schema)
    def get(self, id):
        return ExampleModel.query.get(id)

    @example_namespace.expect(example_input_schema)
    @example_namespace.marshal_with(example_schema)
    def patch(self, id):
        example = ExampleModel.query.get(id)
        example.name = example_namespace.payload["name"]
        db.session.commit()
        return example

    def delete(self, id):
        example = ExampleModel.query.get(id)
        db.session.delete(example)
        db.session.commit()
        return {}, 204