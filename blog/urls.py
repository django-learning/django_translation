from django.conf.urls import i18n
from django.urls import path
from .views import blog_view, blog_ajax_view

urlpatterns = [
    path('', blog_view, name="blog_index"),
    path('ajax_index', blog_ajax_view, name="blog_ajax_index")
]