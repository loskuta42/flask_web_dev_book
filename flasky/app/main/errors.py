from http import HTTPStatus

from flask import render_template, request, jsonify
from . import main


@main.app_errorhandler(HTTPStatus.FORBIDDEN)
def forbidden(e):
    if (request.accept_mimetypes.accept_json
            and not request.accept_mimetypes.accept_html):
        response = jsonify({'error': 'forbidden'})
        response.status_code = HTTPStatus.FORBIDDEN
        return response
    return render_template('403.html'), HTTPStatus.FORBIDDEN


@main.app_errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(e):
    if (request.accept_mimetypes.accept_json
            and not request.accept_mimetypes.accept_html):
        response = jsonify({'error': 'not found'})
        response.status_code = HTTPStatus.NOT_FOUND
        return response
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@main.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(e):
    if (request.accept_mimetypes.accept_json
            and not request.accept_mimetypes.accept_html):
        response = jsonify({'error': 'internal server error'})
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return response
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
