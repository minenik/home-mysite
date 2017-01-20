from django.conf.urls import *
from mysite.blog.views import archive

urlpatterns = [

url(r'^$', archive),

]
