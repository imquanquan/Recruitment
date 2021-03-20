from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import Resume
from ..serializers import ResumeSerializer
from ..permissions import IsOwnerOrReadOnly


class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_hunter_name', 'age', 'sex', 'education',
                        'telephone', 'intention', 'job_hunter_id']


class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
