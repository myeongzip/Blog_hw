from rest_framework import serializers
from accounts.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):   # 요기 아예 모르겠음. validated_data -> is_valid()거친 data
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)   # 해싱
        user.save()
        return user