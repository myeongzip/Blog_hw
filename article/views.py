from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from article.serializers import ArticleCreateSerializer, ArticleListSerializer, ArticleSerializer
from article.models import Article

# Create your views here.

class ArticleView(APIView): 
    def get(self, request): # 최초 read 확인
        articles = Article.objects.all()
        print(articles)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
