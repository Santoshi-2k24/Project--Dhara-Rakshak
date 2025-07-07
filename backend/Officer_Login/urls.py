from django.urls import path
from .views import OfficerLoginView, OfficerCreateView

urlpatterns = [
    path('officer_login/', OfficerLoginView.as_view(), name='officer-login'),
    path('create_officer/', OfficerCreateView.as_view(), name='officer-create'),
]
