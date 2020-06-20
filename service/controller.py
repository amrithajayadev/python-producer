import os

from flask import Flask, jsonify, request
from flask_restplus import Api, Resource

from service import producerService
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.route('/')
def hello():
    return jsonify("A sample python producer app for testing pact")


def prepare_state(param):
    pass


@app.route('/pact/provider_states', methods=['GET', 'POST'])
def states():
    """ USAGE: python-verifier will send a request with the body:
               {consumer: 'Consumer name', states: ['a thing exists']}
               to this enpoint. One state at the time is allowed.
    """
    data = request.get_json()
    prepare_state(data["states"][0])
    return jsonify({"productName": "Laptops", "locationName": "Bangalore", "quantity": 1000})


api = Api(
    app,
    version='1.0.0',
    title='python-producer',
    description='A sample python producer app for testing pact',
    doc='/apidocs',
    serve_challenge_on_401=True)

ns = api.namespace('api')


@ns.route("/inventory")
class PipelineState(Resource):
    """
    Class that exposes APIs to get and set the inventory.
    """

    def get(self):
        try:
            response = producerService.get_inventory()
            return jsonify(response)
        except Exception as e:
            logger.error("/api/inventory - [GET] - Unexpected error: %s", e.description)

    def post(self):
        try:
            logger.debug('Received inventory data: %s', request.get_json())
            response = producerService.save_inventory(request.get_json())
            return jsonify(response)
        except Exception as e:
            logger.error("/api/inventory - [POST] - Unexpected error: %s", e)


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=int(os.getenv("PORT", 9099)))
    except Exception as err:
        logger.error("trace:", exc_info=True)
