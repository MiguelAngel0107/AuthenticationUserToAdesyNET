from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.contrib.auth import get_user_model
User = get_user_model()
from apps.user.serializers import UserSerializer



class RegisterUser(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request, format=None):
        data = self.request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        access_code = data.get('access_code')

        if not first_name or not password or not access_code or not last_name:
            return Response({'error': 'All fields are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            password=password, 
            access_code=access_code
            )
        return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)


class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

