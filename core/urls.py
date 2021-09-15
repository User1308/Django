from django.urls import path
from .views import HomePageView, BookDetailView, BookCreationView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('write/', BookCreationView.as_view(), name='book-creation'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]
