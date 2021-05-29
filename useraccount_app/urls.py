from django.urls import path
from useraccount_app.views import profile_list, profile_edit, UserLogin, signup_view, send_confirm_email
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from useraccount_app.forms import MyChangePasswordForm

app_name = "useraccount_app"

urlpatterns = [

    path("profile-list/", profile_list, name="profile_list"),
    path("profile-edit/<int:id>/", profile_edit, name="profile_edit"),
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", signup_view, name="register"),
    path("send-mail/", send_confirm_email, name="send_mail"),
    path("logout/", LogoutView.as_view(next_page='/useraccount-app/login/'), name="logout"),
    path("change-password/", PasswordChangeView.as_view(template_name="change_password.html", form_class=MyChangePasswordForm), name="change_password"),
    path("password-change-done/", PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name="password_change_done"),
]