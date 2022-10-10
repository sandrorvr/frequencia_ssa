from django.urls import path
from .views import EscalaAPIView

urlpatterns = [
    path('worker/<str:worker>', EscalaAPIView.as_view(), name='escala'),
]
