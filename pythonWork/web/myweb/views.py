from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json
# 定义视图函数，业务逻辑
# def index(request):

    # 返回一句话
    # return HttpResponse('开发中.....')


from .models import Class_lists,Class_details,Class_top

def classList(request):
	# 加载一个模块
	classes = Class_lists.objects.all()[:4].values()
	# print(classes[0])
	return render(request,'classList.html',{'classes':classes})

def classDetails(request):
	detail_id = request.GET.get('detailid')
	# print('参数：',detail_id)
	return render(request,'classDetails.html',{'detail_id':detail_id})

def videos(request):
	detail_id = request.GET.get('detail_id')
	page = int(request.GET.get('page'))
	# print(detail_id)
	# print(page)
	data = list(Class_details.objects.filter(detail_id=detail_id).values())
	data =data[page]
	# print(data)
	return HttpResponse(json.dumps(data))