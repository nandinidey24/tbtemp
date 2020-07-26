from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.loguser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signup, name="signup"),
    path('resetPasswordQuestions', views.resetPasswordQuestions, name="resetPasswordQuestions"),
    path('resetPassword', views.resetPassword, name="resetPassword"),
    path('subject', views.subject, name="subject"),
    path('document', views.document, name="document")
]