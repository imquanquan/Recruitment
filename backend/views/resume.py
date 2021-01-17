from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import Resume
from ..serializers import ResumeSerializer


class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_hunter_name', 'age', 'sex', 'education',
                        'telephone', 'intention', 'job_hunter_id']


class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
