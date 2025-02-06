from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User

class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
