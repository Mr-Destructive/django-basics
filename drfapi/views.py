from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer
from .models import Article
from .forms import ArticleForm

class CreateArticle(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        form = ArticleForm()
        return Response({'form': form}, template_name='drfapi/create.html')

    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save(author=request.user)
            return Response({'article':serializer.data}, template_name='drfapi/task.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateArticle(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk, format=None):
        form = ArticleForm()
        return Response({'form': form}, template_name='drfapi/update.html')

    def post(self, request, pk, format=None):
        task = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=task, data=request.data)
        if(serializer.is_valid()):
            serializer.save(author=request.user)
            return Response({'tasks':serializer.data}, template_name='drfapi/task.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteArticle(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request,pk, format=None):
        task = Article.objects.get(id=pk)
        task.delete()
        tasks = Article.objects.filter(author=request.user)
        serializer = ArticleSerializer(tasks, many=True)
        return Response({'article':serializer.data}, template_name='index.html')

class Index(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, format=None):
        if request.user.id:
            tasks = Article.objects.filter(author=request.user)
            serializer = ArticleSerializer(tasks, many=True)
            return Response({'article':serializer.data}, template_name='index.html')
        return Response(template_name='index.html')

class GetArticle(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    def get(self, request,pk , format=None):
        tasks = Article.objects.get(id=pk)
        serializer = ArticleSerializer(tasks, many=False)
        return Response({'article':serializer.data}, template_name='drfapi/task.html')

