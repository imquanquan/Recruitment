from django.urls import path

from . import jobhunter

urlpatterns = [
    # 用户相关接口
    # 注册
    path('jobhunter/register', jobhunter.register, name='jobhunter_register'),
    # 登陆
    path('jobhunter/login', jobhunter.login, name='jobhunter_login'),
    # 查看个人信息
    path('jobhunter/<int:jobhunter_id>', jobhunter.info, name='jobhunter_info'),
]