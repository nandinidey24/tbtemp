from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('reset-password-questions', views.reset_password_questions, name="reset-password-questions"),
    path('reset-password', views.reset_password, name="reset-password"),
    path('subject', views.subject, name="subject"),
    path('document', views.document, name="document")
]