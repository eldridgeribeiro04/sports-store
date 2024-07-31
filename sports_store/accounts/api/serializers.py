from rest_framework import serializers
from accounts.models import *

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type': 'password'}, write_only=True)
    
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
            
        if password!=password2:
            raise serializers.ValidationError('Passwords must match.')
            
        if MyUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError('Email already exists.')
        
        if MyUser.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError('Username already exists.')
        
        account = MyUser.objects.create(username=self.validated_data['username'],
                                        email=self.validated_data['email']
            )
        password = self.validated_data.pop('password')
        account.set_password(password)
        account.save()
          
        return account
    
    