from django.urls import path
from useraccount_app.views import profile_list, profile_edit, UserLogin, signup_view, send_confirm_email
from django.contrib.auth.views import LogoutView

app_name = "useraccount_app"

urlpatterns = [

    path("profile-list/", profile_list, name="profile_list"),
    # path("profile-add/", profile_add, name="profile_add"),
    path("profile-edit/<int:id>/", profile_edit, name="profile_edit"),
    # path("profile-delete/<int:id>/", profile_delete, name="profile_delete"),
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", signup_view, name="register"),
    path("send-mail/", send_confirm_email, name="send_mail"),
    path("logout/", LogoutView.as_view(next_page='/useraccount-app/login/'), name="logout"),
]