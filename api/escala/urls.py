from django.urls import path
from .views import EscalaAPIView, WorkersAPIView

urlpatterns = [
    path('<str:worker>', EscalaAPIView.as_view(), name='escala'),
    path('workers/<str:worker>', WorkersAPIView.as_view(), name='workers'),
#    path('footHold/<str:worker>', EscalaAPIView.as_view(), name='escala'),

]
