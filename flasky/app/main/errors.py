from http import HTTPStatus

from flask import render_template
from . import main


@main.app_errorhandler(HTTPStatus.FORBIDDEN)
def forbidden(e):
    return render_template('403.html'), HTTPStatus.FORBIDDEN


@main.app_errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(e):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@main.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(e):
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
