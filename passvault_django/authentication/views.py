from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from .utils import normalize_email
from rest_framework_simplejwt.tokens import RefreshToken

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response ({'token':token, 'msg':'Account Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            normalized_email = normalize_email(serializer.data.get('email'))
            password = serializer.data.get('password')
            user = authenticate(email=normalized_email, password=password)
            if user is not None:
                if user.is_active:
                    token = get_tokens_for_user(user)
                    return Response({'token':token, 'msg':'Login Successful.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error':'The user is deactivated.'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'errors':{'non_field_erors':['Incorrect Credentials.']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)