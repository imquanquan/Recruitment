from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import CollectJob
from ..serializers import CollectJobSerializer


class CollectJobList(generics.ListCreateAPIView):
    queryset = CollectJob.objects.all()
    serializer_class = CollectJobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_hunter_id', 'job_id']


class CollectJobDetail(generics.RetrieveDestroyAPIView):
    queryset = CollectJob.objects.all()
    serializer_class = CollectJobSerializer
