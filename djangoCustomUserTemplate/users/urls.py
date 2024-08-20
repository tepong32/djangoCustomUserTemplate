from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    ### Authentication
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout' ),
    path('register/', register, name='register' ),
    # path('search/', user_search_view, name="user-search"),

    ### Django-Allauth
    path('accounts/', include('allauth.urls')),
    
    ### Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password-change'),

    path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'), name='password-reset'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password-reset-complete'),
]
