"""Django_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('posts/', include('posts.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from users import views as users_views
from . import settings

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add routes for login/logout/register/account
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),
        name="logout",
    ),
    path("account/", users_views.account, name="account"),
    path("register/", users_views.register, name="register"),
    # Routs for posts
    path("", include("posts.urls")),
    # API routes
    url(r"^api/auth/token/", obtain_jwt_token),
    path("api/", include("posts.api.urls")),
    path("api/users/", include("users.api.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
