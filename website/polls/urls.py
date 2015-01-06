from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', "polls.views.index", name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', "polls.views.detail", name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', "polls.views.results", name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
    
    url(r'^hehe$', 'polls.views.hehe', name='hehe'),

)
