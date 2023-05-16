from django.urls import path
from achievements import views

urlpatterns = [
    path('books/read', views.GetBooksAPI.as_view())
]
