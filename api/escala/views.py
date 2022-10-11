from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Escala
from .serializers import EscalaSerializers, WorkersSerializers

import numpy as np

class MatchWorker:
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
            workersMach.append(filtered)
        return workersMach

    def match_to_serializer(self):
        wks_serializers = []
        workersMach = self.get_match()
        for wks in workersMach:
            serializer = EscalaSerializers(wks, many=True)
            wks_serializers.append(serializer.data)

        wks_sz = self.flaten(wks_serializers)
        print(wks_sz)
        return wks_sz

class EscalaAPIView(APIView):
    def get(self, request, worker):
        return Response(MatchWorker(worker).match_to_serializer())

class WorkersAPIView(APIView):
    def get(self, request, worker):
        matchWorker = MatchWorker(worker)
        matchWorkerMatch= matchWorker.get_match()
        workersName = []
        for wk in matchWorkerMatch:
            workersName.append(WorkersSerializers(wk, many=True).data)
        return Response(matchWorker.flaten(workersName))
