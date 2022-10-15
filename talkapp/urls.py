from django.urls import path
from .import views

urlpatterns=[
    path("", views.index, name="Home"),
    path("loginpage/",views.loginpage, name="loginpage"),
    path("handle_login/",views.handle_login, name="handle_login"),
    path("userpage/",views.userpage, name="userpage"),
    path("handle_logout/",views.handle_logout, name="handle_logout"),
    path("message/<int:id>",views.message,name="message"),
    path("make_entry/",views.make_entry, name="make_entry"),
    path("send/",views.send, name="send"),


]