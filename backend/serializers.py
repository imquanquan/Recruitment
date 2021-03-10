from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.db import transaction

from .models import *


class JobHunterCustomRegistrationSerializer(RegisterSerializer):
    # 引用 model 的字段
    job_hunter = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    jobhuntername = serializers.CharField(required=True)
    age = serializers.IntegerField()
    sex = serializers.CharField()

    def get_cleaned_data(self):
        """
        重写 get_cleaned_data 方法，除了获取 user 自带字段还获取 jobhunter 的字段
        :return:
        """
        data = super(JobHunterCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'age': self.validated_data.get('age', ''),
            'jobhuntername': self.validated_data.get('jobhuntername', ''),
            'sex': self.validated_data.get('sex', ''),
        }
        data.update(extra_data)
        return data

    @transaction.atomic
    def save(self, request):
        """
        重写 save 方法，除了更新 user 表，还更新 jobhunter 表
        :param request:
        :return:
        """
        user = super(JobHunterCustomRegistrationSerializer, self).save(request)
        user.is_job_hunter = True
        user.save()
        job_hunter = JobHunter(job_hunter=user,
                               jobhuntername=self.cleaned_data.get('jobhuntername'),
                               age=self.cleaned_data.get('age'),
                               sex=self.cleaned_data.get('sex'))
        job_hunter.save()
        return user


class CompanyRegistrationSerializer(RegisterSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    companyname = serializers.CharField(required=True)
    address = serializers.CharField()

    def get_cleaned_data(self):
        data = super(CompanyRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'address': self.validated_data.get('address', ''),
            'companyname': self.validated_data.get('companyname', ''),
        }
        data.update(extra_data)
        return data

    @transaction.atomic
    def save(self, request):
        user = super(CompanyRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(company=user,
                          companyname=self.cleaned_data.get('companyname'),
                          address=self.cleaned_data.get('address'))
        company.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'address', 'companyname')


class JobHunterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHunter
        fields = ('id', 'age', 'sex', 'jobhuntername')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_name', 'description', 'salary', 'education', 'company_id')


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'job_hunter_name', 'age', 'sex', 'education',
                  'telephone', 'intention', 'description', 'job_hunter_id')


class CollectJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectJob
        fields = ('id', 'job_hunter_id', 'job_id')


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = ('id', 'job_hunter_id', 'job_id', 'resume_id', 'deliver_date')
