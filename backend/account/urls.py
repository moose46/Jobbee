from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.reqister, name="register"),
]
