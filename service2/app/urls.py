from django.urls import path

from .views import BooksView, BooksListView

urlpatterns = [
    path('books/', BooksListView.as_view()),
]