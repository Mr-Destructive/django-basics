from django.urls import path
from .views import (
        CreateArticle,UpdateArticle, DeleteArticle, 
        Index, GetArticle
        )
from django.views.generic import TemplateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:pk>', GetArticle.as_view(), name='task'),
    path('create/', CreateArticle.as_view(), name='createtask'),
    path('update/<str:pk>', UpdateArticle.as_view(), name='updatetask'),
    path('delete/<str:pk>', DeleteArticle.as_view(), name='deletetask'),
]
