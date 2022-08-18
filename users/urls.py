from django.urls import path
from users import views

from users.views import UserSignUpView, UserLoginView, VerifyEmailView, PasswordRecoveryEmail, SetNewPasswordView

urlpatterns = [
	path('signup/', views.UserSignUpView.as_view(),),
	path('email-verify/', views.VerifyEmailView.as_view(), name="email-verify"),
	path('login/', views.UserLoginView.as_view()),
	path('password-reset/', views.PasswordRecoveryEmail.as_view(), name="password-reset"),
	path('password-reset-complete/', views.SetNewPasswordView.as_view(), name='password-reset-complete'),
]