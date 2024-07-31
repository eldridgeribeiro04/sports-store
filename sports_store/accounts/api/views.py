from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import viewsets, status

from accounts.api.serializers import RegistrationSerializer


class CreateUserView(APIView):
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            token, created = Token.objects.get_or_create(user=account)
            
            data = {'response': 'User created successfully',
                'username': account.username,
                'email': account.email,
                'token': token.key
                }
            
            return Response(data, status=status.HTTP_201_CREATED)
        
        data = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
        
class LogoutAPIView(APIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

