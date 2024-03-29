from http import HTTPStatus

from flask import jsonify
from app.exceptions import ValidationError
from . import api


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = HTTPStatus.BAD_REQUEST
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = HTTPStatus.UNAUTHORIZED
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = HTTPStatus.FORBIDDEN
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
