from django.urls import path
from django.conf.urls import url
from .views.auth import JobHunterRegistrationView, CompanyRegistrationView
from .views.jobhunter import JobHunterList, JobHunterDetail, JobHunterToJobList
from .views.company import CompanyList, CompanyDetail
from .views.job import JobDetail, JobList, JobToJobHunterList
from .views.resume import ResumeList, ResumeDetail
from .views.collectjob import CollectJobDetail, CollectJobList
from .views.deliver import DeliverDetail, DeliverList

app_name = 'backend'


urlpatterns = [
    # 两类认证地址
    path('registration/company', CompanyRegistrationView.as_view(), name='register-company'),
    path('registration/jobhunter', JobHunterRegistrationView.as_view(), name='register-jobhunter'),
    # 求职者相关操作地址
    url('^jobhunter$', JobHunterList.as_view()),
    url(r'^jobhunter/(?P<pk>[0-9]+)$', JobHunterDetail.as_view()),
    url(r'^jobhunter/(?P<pk>[0-9]+)/collectjobs$', JobHunterToJobList.as_view()),
    # 公司相关操作地址
    url('^company$', CompanyList.as_view()),
    url(r'^company/(?P<pk>[0-9]+)$', CompanyDetail.as_view()),
    # 工作相关操作地址
    url('^job$', JobList.as_view()),
    url(r'^job/(?P<pk>[0-9]+)$', JobDetail.as_view()),
    url(r'^job/(?P<pk>[0-9]+)/collectjobhunters$', JobToJobHunterList.as_view()),
    # 简历相关操作地址
    url('^resume$', ResumeList.as_view()),
    url(r'^resume/(?P<pk>[0-9]+)$', ResumeDetail.as_view()),
    url('^collectjob$', CollectJobList.as_view()),
    url(r'^collectjob/(?P<pk>[0-9]+)$', CollectJobDetail.as_view()),
    url('^deliver$', DeliverList.as_view()),
    url(r'^deliver/(?P<pk>[0-9]+)$', DeliverDetail.as_view()),
]
