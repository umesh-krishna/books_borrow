from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.serializers import *
from rest_framework import generics, views as rest_views
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


User = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class LoginAPI(rest_views.APIView):
    def post(self, request):
        data = request.data
        if 'email' not in data or 'password' not in data:
            return JsonResponse({'message': 'Bad Request'}, status=400)
        try:
            user = User.objects.get(email=data.get('email'))
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid email'}, status=401)
        if user.check_password(data.get('password')):
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)
        return JsonResponse({'message': 'Wrong password'}, status=401)