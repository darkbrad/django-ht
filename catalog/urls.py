from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path("author",views.AuthorListView.as_view(),name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author"),
    path("author/create", views.AuthorCreateView.as_view(), name="author-create"),
    path(
        "author/update/<int:pk>", views.AuthorUpdateView.as_view(), name="author-update"
    ),
    path(
        "author/delete/<int:pk>", views.AuthorDeleteView.as_view(), name="author-delete"
    ),
]
