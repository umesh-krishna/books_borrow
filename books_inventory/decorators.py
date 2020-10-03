from functools import wraps
from django.http import JsonResponse


def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            user = request.request.auth.user
            request.user = user
            return function(request, *args, **kwargs)
        except:
            return JsonResponse({}, status=401)

    return wrap
