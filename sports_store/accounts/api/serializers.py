from accounts.models import MyUser
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = MyUser
        fields = ("username", "email", "password", "password2")
        
    def save(self, request):
        password = self.validated_data['password']
        password2 = self.validated_data['password']
        
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        
        if MyUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists."})
        
        elif MyUser.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({"username": "Username already exists."})
        
        account = MyUser.objects.create_user(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        
        return account
            