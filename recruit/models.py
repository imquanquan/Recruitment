from django.db import models


class Company(models.Model):
    CName = models.CharField(max_length=100)
    Caddress = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Job(models.Model):
    JName = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    salary = models.IntegerField()
    Ebackground = models.CharField(max_length=100)


class JobHunter(models.Model):
    age = models.IntegerField()
    HName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)


class Resume(models.Model):
    job_hunter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    Hname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    Ebackground = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    jobIntention = models.CharField(max_length=100)


class Interview(models.Model):
    job_hunter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Itime = models.DateTimeField()
    Iaddress = models.CharField(max_length=100)


class Deliver(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class CollectResume(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class CollectJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_counter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)