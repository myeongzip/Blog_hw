from tokenize import TokenError
from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import action

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):   # 요기 아예 모르겠음. validated_data -> is_valid()거친 data
        user = super().create(validated_data)
        user.set_password(validated_data['password'])   # 비밀번호 해싱
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):   # jwt token의 payload에 username과 fullname 추가
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['fullname'] = user.fullname

        return token

class RefreshTokenSerializer(serializers.Serializer):   # refresh token을 이용해 로그아웃 기능을 위해 만듦.
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": "Token is invalid or expired"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None

    def validate(self, attrs):
        self.token = attrs["refresh"]
        try:
            # Try to create a RefreshToken object. If the token is invalid, it will raise an exception.
            RefreshToken(self.token)
        except TokenError:
            self.fail("bad_token")
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")