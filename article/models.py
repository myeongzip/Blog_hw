from django.db import models

from Blog import settings

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True, default="-")
    created_at = models.DateTimeField(auto_now_add=True) # 최초로 object를 만드는 필드에 쓰는 auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)      # 필드가 업데이트되지 않고, object의 value를 수정할 때 명시함
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")  # related_name 지정 안 했을 때 author._set -> 특정 user가 쓴 모든 글 불러오기
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_article", symmetrical=False, )
    
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") # related_name 지정 안 했을 때 article._set -> article의 모든 comment들 불러오기
    
    def __str__(self):
        return str(self.content)