from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Job
from ..serializers import JobSerializer, JobHunterSerializer
from ..permissions import IsOwnerOrReadOnly


class JobList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['education', 'salary', 'description', 'job_name', 'welfare', 'experience', 'company_id']


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobToJobHunterList(generics.ListAPIView):
    serializer_class = JobHunterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['age', 'jobhuntername', 'sex']

    def get_queryset(self):
        print(self.kwargs['pk'])
        job = Job.objects.get(pk=self.kwargs['pk'])
        return job.collect_set.all()
