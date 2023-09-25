from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name="signup_view"),
    
]