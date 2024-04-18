
from django.urls import path

from .views import ProductView

urlpatterns = [
    path('api/v1/product/', ProductView.as_view()),
]