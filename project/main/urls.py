from django import views
from django.urls import include, path
from. import views

app_name="main"

urlpatterns = [
    path('home/',views.home,name='home_page'),
    path('article/',views.article_details,name='article_details'),
    path('sumaiya-sani/',views.my_cv,name='my_cv'),
   
]