from django.urls import path
from . import views
# from blogapp.views import api_detail_blog_view

urlpatterns = [
    path('<slug>/',views.api_detail_blog_view,name="detail"),
]