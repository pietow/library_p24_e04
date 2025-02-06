from rest_framework.serializers import ModelSerializer
from books.models import Book
from django.contrib.auth.models import User

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'author', ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'