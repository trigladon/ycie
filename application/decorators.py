from functools import wraps

from django.http import Http404


def ajax(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[1].is_ajax:
            raise Http404()
        return func(*args, **kwargs)
    return wrapper