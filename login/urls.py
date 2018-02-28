from django.contrib import admin
from django.urls import path
from django.conf.urls import include , url
from . import views

urlpatterns = [
    url('^$', views.login),
    url('^loggedin/$', views.loggedin),
    url('^auth/$', views.auth),
    url('^loggedin/addcourset/$', views.addct),
    url('^loggedin/selectcourse/$', views.selectprof),
    url('^loggedin/selectcourse/addcs/$', views.addcs),
    url('^loggedin/deletecourse/$', views.removesc),
    url('^logout/$', views.logout),
    url('^deletetc/$', views.deletetc),
    url('^addmessage/$', views.addmessage),
    url('^sendmessage/$',views.addmessage),
    url('^studentmsg/$',views.studentmessage)
]
