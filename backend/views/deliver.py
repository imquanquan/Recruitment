from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import Deliver
from ..serializers import DeliverSerializer


class DeliverList(generics.ListCreateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_hunter_id', 'job_id']


class DeliverDetail(generics.RetrieveDestroyAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
