from django.urls import path
from .views import RegistrationView, LoginView, ActivationView, LogoutView, ChangePasswordView, ForgotPasswordView, ForgotPasswordCompleteView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('changepass/',ChangePasswordView.as_view()),
    path('forgotpass/',ForgotPasswordView.as_view()),
    path('forgotpasscompl/', ForgotPasswordCompleteView.as_view())
]

