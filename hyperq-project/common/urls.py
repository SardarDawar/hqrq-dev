
from django.urls import path, re_path
from .views import (home, about, faq, support, policy)
from django.contrib.auth import views as auth_views
from users.views import (deleteAccount_AJAX, emailVerify, login, register,
                         user_settings, MyPasswordResetView)

# url patterns under ('')
urlpatterns = [

    # base site urls
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('support/', support, name='support'),
    path('policy/', policy, name='policy'),

    # user app login/logout and signup urls
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # user/profile action urls
    path('settings/', user_settings, name='settings'),
    path('settings/delete/', deleteAccount_AJAX, name="account-delete"),
    path('email_verify/<uidb64>/<token>/', emailVerify, name='email-verify'),

    # user password-reset urls
    path('password-reset/', MyPasswordResetView.as_view(template_name='users/password.reset/password_reset.html'), name='password_reset'),
    path('password-reset/requested/', auth_views.PasswordResetDoneView.as_view(template_name='users/password.reset/done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password.reset/confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password.reset/complete.html'), name='password_reset_complete'),

]
