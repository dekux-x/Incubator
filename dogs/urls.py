from django.urls import path

from . import views

app_name = 'dogs'

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:breed>/", views.detail, name = 'detail'),
]
