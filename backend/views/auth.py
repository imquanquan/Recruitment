from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from ..serializers import (
    CompanyRegistrationSerializer, JobHunterCustomRegistrationSerializer
    )


class JobHunterRegistrationView(RegisterView):
    serializer_class = JobHunterCustomRegistrationSerializer


class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyRegistrationSerializer
