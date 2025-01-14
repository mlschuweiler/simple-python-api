from flask_restx import Api

api = Api(
    prefix='/',
    version='1.0.0',
    title='Simple Python Api',
    description='REST API showcasing how to use python as the framework used to serve an API',
    # doc=None,
) # security='Bearer'
