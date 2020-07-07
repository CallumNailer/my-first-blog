from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('cv', views.cv, name='cv'),
    path('Gallery', views.gallery, name='gallery')
]
