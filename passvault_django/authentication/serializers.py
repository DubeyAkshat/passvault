from rest_framework import serializers
from .models import User
import re
from .utils import normalize_email

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs ):
        email = attrs.get('email')
        username = attrs.get('username')
        username_pattern = r"^\w+$"
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if User.objects.filter(email=normalize_email(email)).exists():
            raise serializers.ValidationError("Email address already in use.")
        if not re.match(username_pattern, username):
            raise serializers.ValidationError("Username can only contain letters, numbers and underscores.")
        if User.objects.filter(username=username.strip().lower()).exists():
            raise serializers.ValidationError("Username already in use.")
        if(password != password2):
            raise serializers.ValidationError("Password and Confirm Password don't match.")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)