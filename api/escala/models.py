from django.db import models

class Escala(models.Model):
    g1 = 'i'
    g2 = 'ii'
    g3 = 'iii'
    g4 = 'iv'
    group = models.CharField(
        'Group', 
        max_length=3, 
        choices=[
            (g1, 'Grupo_1'),
            (g2, 'Grupo_2'),
            (g3, 'Grupo_3'),
            (g4, 'Grupo_4'),
            ],
        default = g1
        )
    
    vtr = 'vtr'
    motorcycle = 'mt'
    equipment = models.CharField(
        'Equipment', 
        max_length=3, 
        choices=[
            (vtr, 'Viatura'),
            (motorcycle, 'Moto'),
            ],
        blank=True
        )
    
    date = models.DateField('Date')
    road = models.CharField('Road', max_length=20)
    begin = models.TimeField('Begin')
    end = models.TimeField('End')
    foothold = models.CharField('FootHold', max_length=250)
    worker = models.CharField('Worker', max_length=120)
    zone = models.CharField('Zone', max_length=20)

