from django.urls import path
from django.conf.urls import url
from .views.auth import JobHunterRegistrationView, CompanyRegistrationView
from .views.jobhunter import JobHunterList, JobHunterDetail, JobHunterToJobList
from .views.company import CompanyList, CompanyDetail
from .views.job import JobDetail, JobList
from .views.resume import ResumeList, ResumeDetail


app_name = 'backend'


urlpatterns = [
    path('registration/company', CompanyRegistrationView.as_view(), name='register-company'),
    path('registration/jobhunter', JobHunterRegistrationView.as_view(), name='register-jobhunter'),
    url('^jobhunter$', JobHunterList.as_view()),
    url(r'^jobhunter/(?P<pk>[0-9]+)$', JobHunterDetail.as_view()),
    url(r'^jobhunter/(?P<pk>[0-9]+)/collectjobs$', JobHunterToJobList.as_view()),
    url('^company$', CompanyList.as_view()),
    url(r'^company/(?P<pk>[0-9]+)$', CompanyDetail.as_view()),
    url('^job$', JobList.as_view()),
    url(r'^job/(?P<pk>[0-9]+)$', JobDetail.as_view()),
    url('^resume$', ResumeList.as_view()),
    url(r'^resume/(?P<pk>[0-9]+)$', ResumeDetail.as_view()),
]
