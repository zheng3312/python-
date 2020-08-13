from django.conf.urls import url
from django.contrib import admin

from book import views
from book.views import set_cookie,get_cookie,set_session,HomeView

urlpatterns = [
    # url(r'^index/$',index),
    # url(r'^1/100/$',views.index),
   # url(r'^(\d+)/(\d+)/$',index),
    url(r'^set_cookie',set_cookie),
    url(r'^get_cookie', get_cookie),
    url(r'set_session', set_session),
    url(r'^login/$',views.LoginView.as_view()),
    url(r'^home/$',views.HomeView.as_view()),
]
