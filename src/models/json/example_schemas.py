from flask_restx import fields

from api import api

example_schema = api.model("ExampleModel", {
    "id": fields.Integer(readonly=True, description="Unique identifier of the example object"),
    "name": fields.String(description="name of the example object"),
})

example_input_schema = api.model("ExampleInput", {
    "name": fields.String,
})