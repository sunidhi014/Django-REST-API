from rest_framework import viewsets
from . import models
from . import serializer

class JobViewset(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializer.JobSerializer