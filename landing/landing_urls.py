from django.urls import path
from landing import views

urlpatterns = [
    path("", views.homepage),
    path("templates/", views.landing),
]
