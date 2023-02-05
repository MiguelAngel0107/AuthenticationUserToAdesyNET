from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model
User = get_user_model()



class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        access_code = request.data.get('access_code')

        if not username or not password or not access_code:
            return Response({'error': 'All fields are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, access_code=access_code)
        return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)
