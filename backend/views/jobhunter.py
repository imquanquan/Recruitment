from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ..models import JobHunter
from ..serializers import JobHunterSerializer, JobSerializer


class JobHunterList(generics.ListAPIView):
    queryset = JobHunter.objects.all()
    serializer_class = JobHunterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['age', 'jobhuntername', 'sex']


class JobHunterDetail(generics.RetrieveUpdateAPIView):
    queryset = JobHunter.objects.all()
    serializer_class = JobHunterSerializer


class JobHunterToJobList(generics.ListAPIView):
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['education', 'salary', 'description', 'job_name', 'company_id_id']

    def get_queryset(self):
        print(self.kwargs['pk'])
        job_hunter = JobHunter.objects.get(pk=self.kwargs['pk'])
        return job_hunter.collect_jobs.all()
