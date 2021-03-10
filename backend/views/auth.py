from django.shortcuts import render

# Create your views here.

"""
重写注册 view，对象为 Jobhunter 和 Company
"""


from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from ..serializers import (
    CompanyRegistrationSerializer, JobHunterCustomRegistrationSerializer
    )


class JobHunterRegistrationView(RegisterView):
    serializer_class = JobHunterCustomRegistrationSerializer


class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyRegistrationSerializer
