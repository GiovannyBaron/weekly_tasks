from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("logout/", views.sign_out, name="logout"),
]