from django.urls import path
from .views import EscalaAPIView

urlpatterns = [
    path('/<str:worker>', EscalaAPIView.as_view(), name='escala'),
    path('workers/<str:worker>', , name='escala'),
    path('footHold/<str:worker>', EscalaAPIView.as_view(), name='escala'),

]
