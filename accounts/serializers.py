from rest_framework import serializers
from accounts.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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