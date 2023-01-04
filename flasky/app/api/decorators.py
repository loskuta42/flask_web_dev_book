from functools import wraps

from flask import g

from .errors import forbidden
from ..models import Post, Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def is_post_author(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        post = Post.query.get_or_404(*args, **kwargs)
        if g.current_user != post.author and not g.current_user.can(Permission.ADMIN):
            return forbidden('Insufficient permissions')
        return func(*args, **kwargs)
    return decorated_function
