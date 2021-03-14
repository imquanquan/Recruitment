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
    logo = models.TextField(default='../assets/scau.jpeg')
    scale = models.CharField(max_length=50, default='0-15', choices=[
        ('0-15', '少于 15 人'),
        ('15-50', '15 - 50 人'),
        ('50-150', '50 - 150 人'),
        ('150-500', '150 - 500 人'),
        ('500-2000', '500 - 2000 人'),
        ('2000-', '2000 人以上')
    ])
    financing = models.CharField(max_length=50, default='none', choices=[
        ('none', '未融资'),
        ('angel', '天使轮'),
        ('a', 'A 轮'),
        ('b', 'B 轮'),
        ('c', 'C 轮'),
        ('d', 'D 轮以上'),
        ('d', 'D 轮以上'),
        ('listed', '上市公司'),
        ('not_need', '不需要融资')
    ])

    def __str__(self):
        return self.company.email


class Job(models.Model):
    job_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    welfare = models.CharField(max_length=50)
    salary = models.CharField(max_length=50, default='0-2000', choices=[
        ('0-2000', '2k 以下'),
        ('2000-5000', '2k-5k'),
        ('5000-10000', '5k-10k'),
        ('10000-15000', '10k-15k'),
        ('15000-25000', '15k-25k'),
        ('25000-50000', '25k-50k'),
        ('50000-', '50k 以上')
    ])
    experience = models.CharField(max_length=50, default='', choices=[
        ('new', '在校/应届'),
        ('0-3', '3 年以下'),
        ('3-5', '3-5 年'),
        ('5-10', '5-10 年'),
        ('10-', '10 年以上'),
        ('none', '无要求')
    ])
    education = models.CharField(max_length=100)
    deliver_date = models.DateField(auto_now_add=True, blank=True)


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

