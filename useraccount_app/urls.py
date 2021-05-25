from django.urls import path
from useraccount_app.views import UserLogin, signup_view
from django.contrib.auth.views import LogoutView

app_name = "useraccount_app"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", signup_view, name="register"),
    # path("send-mail/", send_confirm_email, name="send_mail"),
    path("logout/", LogoutView.as_view(next_page='/useraccount-app/login/'), name="logout"),
]