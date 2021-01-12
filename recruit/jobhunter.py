"""
这里写 jobhunter（求职者）相关业务处理逻辑
"""
import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import JobHunter


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    """
    求职者注册
    :param request:
    :return:
    """
    response = {}
    try:
        jobhunter = JobHunter(**json.loads(request.body))
        jobhunter.save()
        response = model_to_dict(jobhunter)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


def login(request):
    """
    求职者登陆
    :param request:
    :return:
    """
    pass


def info(request, jobhunter_id):
    """
    求职者详细信息
    :param request:
    :param jobhunter_id:
    :return:
    """
    response = {}
    try:
        jobhunter = JobHunter.objects.get(pk=jobhunter_id)
        response = model_to_dict(jobhunter)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

