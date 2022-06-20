from django.urls import path
from rest_framework import routers
from django.urls import path, include, re_path
from . import views
app_name = "main"
router = routers.SimpleRouter()
router.register(r'employees', views.EmployeesViewSet)

urlpatterns = [
    path("", views.Main, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]