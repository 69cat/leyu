from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myweb.models import Class_lists,Class_details,Class_top,Admin_user

import os

def index(request):

 
    return render(request,'myadmin_templates/index.html')

def login(request):
	return render(request,'myadmin_templates/login.html')


def dologin(request):
	passwordlist = []
	admin_name = request.POST.get('admin_name')
	admin_password = request.POST.get('admin_password')
	# print('账号：',admin_name)
	# print('密码：',admin_password)
	password = Admin_user.objects.filter(admin_name=admin_name).values()
	for x in password:
		passwordlist.append(x['admin_password'])
	# print(passwordlist)
	if admin_password in passwordlist:
		# print(admin_password)
		request.session['admin_name'] = admin_name
		request.session['admin_password'] = admin_password
		return render(request,'myadmin_templates/index.html')
	else:
		return render(request,'myadmin_templates/login.html')

def outlogin(request):
	request.session.flush()
	return render(request,'myadmin_templates/login.html')


def catalog(request):
	id = request.GET.get('id')
	return render(request,'myadmin_templates/catalog.html',{'id':id})



def catalog_look(request):
	data = list(Class_lists.objects.all().values())
	# print(data)
	return render(request,'myadmin_templates/catalog_look.html',{'data':data})

def catalog_list(request):
	list_img = request.FILES.get('pic')
	list_name = request.POST.get('name')
	list_text = request.POST.get('descr')
	list_url = request.POST.get('urlid')
	id = request.POST.get('id')
	# print(id)
	if list_img==None:
            return HttpResponse('<script>history.back(-1);</script>')
	destination = open("./static/image/"+str(list_img),"wb+")
	# print(list_img.chunks())
	for chunk in list_img.chunks():
		destination.write(chunk)
	destination.close()
	if id == '':
		obj = Class_lists(list_img=list_img,list_name=list_name,list_text=list_text,list_url=list_url)
		obj.save()
	else:
		obj = Class_lists.objects.filter(id=id).update(list_img=list_img,list_name=list_name,list_text=list_text,list_url=list_url)
	data = list(Class_lists.objects.all().values())
	return render(request,'myadmin_templates/catalog_look.html',{'data':data})







def lists(request):
	return render(request,'myadmin_templates/lists.html')

def lists_look(request):
	data = Class_top.objects.all().values()
	return render(request,'myadmin_templates/lists_look.html',{'data':data})

def lists_list(request):
	top_img = request.FILES.get('top_pic')
	# print(top_img)
	if top_img==None:
            return HttpResponse('<script>history.back(-1);</script>')
	destination = open("./static/image/"+str(top_img),"wb+")
	# print(list_img.chunks())
	for chunk in top_img.chunks():
		destination.write(chunk)
	destination.close()
	obj = Class_top(top_img=top_img)
	obj.save()
	data = Class_top.objects.all().values()
	return render(request,'myadmin_templates/lists_look.html',{'data':data})


def lists_num(request):
	detail_id = request.POST.get('id')
	# print(detail_id)
	num = request.POST.get('num')
	# print(num)
	return render(request,'myadmin_templates/lists_video.html',{'detail_id':detail_id,'num':num})

def lists_video(request):
	id = request.GET.get('id')
	# print(id)
	return render(request,'myadmin_templates/lists_video.html',{'id':id})


def show_video(request):
	detail_id = request.POST.get('detail_id')
	num = int(request.POST.get('num'))
	# print(detail_id)
	# print(type(num))
	for x in range(0,num):
		strs = 'detail_video'+str(x)
		detail_video = request.FILES.get(strs)
		destination = open("./static/image/"+str(detail_video),"wb+")
		for chunk in detail_video.chunks():
			destination.write(chunk)
		destination.close()
		obj = Class_details(detail_video=detail_video,detail_id=detail_id)
		obj.save()
	return HttpResponse('<script>alert("课程添加成功");location.href="/myadmin/lists_look/";</script>')


def video_clear(request):
	id = request.GET.get('id')
	Class_top.objects.filter(id=id).delete()
	Class_details.objects.filter(detail_id=id).delete()
	data = Class_top.objects.all().values()
	return render(request,'myadmin_templates/lists_look.html',{'data':data})