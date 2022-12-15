from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission
from http import HTTPStatus


def permission_required(permission):
    def wrapper(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(HTTPStatus.FORBIDDEN)
            return func(*args, **kwargs)

        return wrapped_function

    return wrapper


def admin_required(func):
    return permission_required(Permission.ADMIN)(func)
