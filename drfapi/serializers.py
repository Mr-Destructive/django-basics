from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Article 
        fields = '__all__'
