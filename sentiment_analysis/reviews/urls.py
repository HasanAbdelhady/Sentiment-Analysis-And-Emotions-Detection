from django.urls import path
from . import views

urlpatterns = [
    path('', views.classify_review, name='classify_review'),
]
