from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_render, name="login_render"),
    path("perform_Login", views.perform_login, name="perform_login"),
    path("perform_Logout", views.perform_logout, name="perform_logout"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("newpage", views.newpage, name="newpage"),
]   





