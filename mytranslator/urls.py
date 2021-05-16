from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('source_text/', views.source_text, name='source_text'),
    path('source_speech/', views.source_speech, name='source_speech')
]
