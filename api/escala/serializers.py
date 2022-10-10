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

class MachSerializers(serializers.Serializer):
    date = serializers.DateField()
    road = serializers.CharField(max_length=20)