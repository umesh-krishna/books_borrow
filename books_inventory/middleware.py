from rest_framework.authtoken.models import Token
from django.shortcuts import reverse
from django.http import JsonResponse


class APIAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/') and request.path not in \
                [reverse('accounts:login'), reverse('accounts:create')]:
            token_key = request.META.get('HTTP_AUTHORIZATION')
            if token_key:
                try:
                    token_key = token_key.lstrip('Token ')
                    token = Token.objects.get(key=token_key)
                    response = self.get_response(request)
                    return response
                except Token.DoesNotExist:
                    return JsonResponse({}, status=401)
            return JsonResponse({}, status=401)
        response = self.get_response(request)
        return response
