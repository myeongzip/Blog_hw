from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from accounts.models import User
from rest_framework.decorators import action
from accounts.serializers import CustomTokenObtainPairSerializer, RefreshTokenSerializer, Userserializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.contrib.auth import logout
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

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return Response("로그인 권한 설정된 get 요청입니다.")

# class LogoutView(APIView):        # 토큰을 없애지는 못하는 logout view
#     def post(self, request):
        
#         logout(request)
#         return Response({'message': "Logout successful"})   

class LogoutView(generics.GenericAPIView):  # body에 refresh token을 post로 보내면 refresh token을 blacklist로 보냄.
    serializer_class = RefreshTokenSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args):
        refresh = self.get_serializer(data=request.data)
        refresh.is_valid(raise_exception=True)
        refresh.save()

        user = request.user
        logout(request) # from django.contrib.auth에서 import 했는데 왜 되지..?

        return Response(f"user :{user.username} 로그아웃 성공!!, 토큰을 반납", status=status.HTTP_204_NO_CONTENT)