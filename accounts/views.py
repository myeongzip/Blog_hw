from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.models import User

from accounts.serializers import CustomTokenObtainPairSerializer, Userserializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
# Create your views here.

class UserView(APIView):
    def post(self, request):        # signup
        serializer = Userserializer(data=request.data)  # post일 경우 data = request.data
        if serializer.is_valid():
            serializer.save()
            return Response("회원 가입 완료", status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response("잘못된 요청", status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):   # signin/login
    serializer_class = CustomTokenObtainPairSerializer

