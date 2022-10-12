from pyexpat import model
from unicodedata import east_asian_width
from rest_framework import serializers
from .models import Escala

class EscalaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Escala
        fields = (
        'group',
        'equipment',
        'date',
        'road',
        'begin',
        'end',
        'foothold',
        'worker',
        'zone'
        )

class WorkersSerializers(serializers.Serializer):
    worker = serializers.ListField(child = serializers.CharField(max_length=120))
