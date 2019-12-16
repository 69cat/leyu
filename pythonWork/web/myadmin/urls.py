"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.conf.urls import url,include

from . import views



urlpatterns = [
	url(r'^$',views.login,name="myadmin_login"),
    url(r'^index/',views.index,name="myadmin_index"), 
    url(r'^dologin/',views.dologin,name="myadmin_dologin"),
    url(r'^outlogin/',views.outlogin,name="myadmin_outlogin"),
    url(r'^catalog/',views.catalog,name="myadmin_catalog"),
    url(r'^catalog_look/',views.catalog_look,name="myadmin_catalog_look"),
    url(r'^catalog_list/',views.catalog_list,name="myadmin_catalog_list"),
    url(r'^lists/',views.lists,name="myadmin_lists"),
    url(r'^lists_look/',views.lists_look,name="myadmin_lists_look"),
    url(r'^lists_list/',views.lists_list,name="myadmin_lists_list"),
    url(r'^lists_num/',views.lists_num,name="myadmin_lists_num"),
    url(r'^lists_video/',views.lists_video,name="myadmin_lists_video"),
    url(r'^show_video/',views.show_video,name="myadmin_show_video"),
    url(r'^video_clear/',views.video_clear,name="myadmin_video_clear"),
]

