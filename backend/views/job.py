from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import Job
from ..serializers import JobSerializer, JobHunterSerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['education', 'salary', 'description', 'job_name', 'company_id_id']


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
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
