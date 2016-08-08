from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from login_module import  views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'user_registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login_data/$', views.login_data),
    url(r'^register_user/$', views.register_data),
    url(r'^register_user/login_data$', views.login_data),
    url(r'^register_user/register_success$', views.register_success),
    url(r'^login_data/logged_in_user$', views.logged_in),
    url(r'^admin/', include(admin.site.urls)),
)
