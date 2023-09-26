from rest_framework import serializers

from article.models import Article



class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    # comment_set = CommentSerializer(many=True)  # 정확하게 'comment_set'로 해야 제대로 작동됨. related_name을 지정해줬다면 그걸로 해야 함.
    likes = serializers.StringRelatedField(many=True)   # user의 string field로 나오게 하는 메소드(?)
    
    def get_author(self, obj):
        return obj.author.username
    class Meta:                 # serializer에 많은 기능이 있고 커스터마이징 가능한 기능들이 많지만, 우선 가장 간단한 버전으로 사용.
        model = Article
        fields = "__all__"
        
class ArticleListSerializer(serializers.ModelSerializer):
    pass

class ArticleCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ("title", "image", "content")

