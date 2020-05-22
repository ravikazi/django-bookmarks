from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from account import views as ac_views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    # login / logout urls
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path("logout-then-login/", auth_views.logout_then_login, name="logout-then-login"),

    # change password urls
    path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    # Reset password urls
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password-reset"),
    path("password-reset/done", auth_views.PasswordResetDoneView.as_view(), name="password-reset/done"),
   # path("password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+/)", auth_views.PasswordResetConfirmView.as_view(), name="password-reset/confirm"),
    path("password-reset/complete", auth_views.PasswordResetCompleteView.as_view(), name="password-reset/complete"),

    # User Profile
    path("users/", views.user_list, name="user_list"),
    path("users/<username>", views.user_detail, name="user_detail"),
    path("user/follow/", views.user_follow, name="user_follow"),
]