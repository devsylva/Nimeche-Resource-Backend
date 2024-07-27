from django.urls import path
from .views import BlogView, BlogDetailView, MaterialListView, MaterialDetailView
from .views import ResourceListView, ResourceDetailView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('materials/', MaterialListView.as_view(), name='materials'),
    path('materials/<int:pk>/', MaterialDetailView.as_view(), name='material'),
    path('resources/', ResourceListView.as_view(), name='resources'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource'),
]

