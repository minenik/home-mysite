from django.conf.urls import *
from mysite.dogovor.views import index

urlpatterns = [

url(r'^$', index),

]
