from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("choices/", views.get_choices, name="get_choices"),
]
