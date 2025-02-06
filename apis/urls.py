from django.urls import path
from .views import BookAPIView, UserAPIView


urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
    path("user/", UserAPIView.as_view(), name="user_list")
]