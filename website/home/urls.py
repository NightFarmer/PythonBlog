from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    
    #url(r'^$', include('polls.urls')),
)
