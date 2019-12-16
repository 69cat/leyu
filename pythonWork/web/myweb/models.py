from django.db import models

# Create your models here.



class Class_lists(models.Model):
	list_img = models.CharField(max_length=255)
	list_name = models.CharField(max_length=50)
	list_text = models.CharField(max_length=255)
	list_url = models.CharField(max_length=255)



class Class_details(models.Model):
	detail_video = models.CharField(max_length=255)
	detail_id = models.CharField(max_length=255)



class Class_top(models.Model):
	top_img = models.CharField(max_length=255)



class Admin_user(models.Model):
	admin_name = models.CharField(max_length=255)
	admin_password = models.CharField(max_length=255)
