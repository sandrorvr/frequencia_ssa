from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Escala
from .serializers import EscalaSerializers, MachSerializers

import numpy as np

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
