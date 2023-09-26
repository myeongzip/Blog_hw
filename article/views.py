from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from article.serializers import ArticleCreateSerializer, ArticleListSerializer, ArticleSerializer, ArticleUpdateSerializer
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView): 
    def get(self, request, article_id): # 최초 read 확인
        article = Article.objects.get(id=article_id)   
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, article_id):
        article = Article.objects.get(id=article_id)  
        serializer = ArticleUpdateSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, article_id): # 최초 read 확인
        article = Article.objects.get(id=article_id) 
        if request.user == article.author:
            article.delete()
            return Response(f"제목 {article.title}인 article 삭제 완료", status=status.HTTP_204_NO_CONTENT)