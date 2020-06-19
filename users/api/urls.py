from django.urls import path

from .views import UserLoginApiView

app_name = "users-api"

urlpatterns = [
    # API login
    path("login/", UserLoginApiView.as_view(), name="login"),
]
