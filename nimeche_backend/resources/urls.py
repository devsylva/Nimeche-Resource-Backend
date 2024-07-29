from django.urls import path
from .views import BlogView, BlogDetailView, MaterialView, MaterialDetailView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('materials/', MaterialView.as_view(), name='materials'),
    path('materials/<int:pk>/', MaterialDetailView.as_view(), name='material')
]

