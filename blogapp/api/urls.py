from django.urls import path,include
from . import views
from rest_framework import routers
from .views import BlogPostViewSet
# from blogapp.views import api_detail_blog_view

router = routers.DefaultRouter()
router.register('list',BlogPostViewSet),

urlpatterns = [
    path('<slug>/', views.api_detail_blog_view, name="detail"),
    path('',include(router.urls))
]