from rest_framework.serializers import ModelSerializer
from .models import BlogContent


class BlogContentSerializer(ModelSerializer):
    class Meta:
        model = BlogContent
        fields = '__all__'
        



