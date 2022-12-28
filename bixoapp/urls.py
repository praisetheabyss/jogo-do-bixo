from django.urls import path

from bixoapp.views import SignUpView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]