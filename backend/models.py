# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_job_hunter = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)


class Company(models.Model):
    company = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.company.email


class Job(models.Model):
    job_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    salary = models.IntegerField()
    education = models.CharField(max_length=100)


class JobHunter(models.Model):
    job_hunter = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    jobhuntername = models.CharField(max_length=100, default='')
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    # 多对多关系
    collect_jobs = models.ManyToManyField(Job, through='CollectJob', related_name='collect_set')
    deliver_jobs = models.ManyToManyField(Job, through='Deliver', related_name='deliver_set')

    def __str__(self):
        return self.job_hunter.email


class Resume(models.Model):
    job_hunter_id = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    job_hunter_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    intention = models.CharField(max_length=100)
    description = models.TextField()


class CollectJob(models.Model):
    """
    多对多关系的表，可添加其他字段，例如收藏日期
    """
    job_hunter_id = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)


class Deliver(models.Model):
    job_hunter_id = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='deliver_job_set')
    resume_id = models.ForeignKey(Resume, on_delete=models.CASCADE)
    deliver_date = models.DateTimeField(auto_now_add=True, blank=True)

