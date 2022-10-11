from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Escala
from .serializers import EscalaSerializers, MachSerializers

import numpy as np

class matchWorker:
    def __init__(self, worker):
        self.worker = worker
        self.sizeMatch = None

    def get_date_road(self):
        fullWorker = Escala.objects.filter(worker=self.worker)
        date = []
        road = []
        for wk in fullWorker:
            date.append(wk.date)
            road.append(wk.road)
        self.sizeMatch = len(date)
        return (date, road)

    @staticmethod
    def flaten(self, vet):
        vet_aux = []
        for sublist in vet:
            for item in sublist:
                vet_aux.append(item)
        return vet_aux

    def get_match(self):
        workersMach = []
        dates, roads = self.get_date_road()
        for i in range(self.sizeMatch):
            filtered = Escala.objects.filter(date=dates[i], road=roads[i]).exclude(worker=self.worker)
            serializer = EscalaSerializers(filtered, many=True)
            workersMach.append(serializer.data)
        return workersMach

class EscalaAPIView(APIView):
    def get(self, request, worker):
        fullWorker = Escala.objects.filter(worker=worker)
        setDate = []
        setRoad = []
        for wk in fullWorker:
            setDate.append(wk.date)
            setRoad.append(wk.road)

        workersMach = []
        for i in range(len(setDate)):
            filtered = Escala.objects.filter(date=setDate[i], road=setRoad[i]).exclude(worker=worker)
            serializer = EscalaSerializers(filtered, many=True)
            workersMach.append(serializer.data)

        _workersMach = []
        for sublist in workersMach:
            for item in sublist:
                _workersMach.append(item)

        return Response(_workersMach)

class workers(APIView):
    def get(self, request, worker):
