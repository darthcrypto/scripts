from django.conf.urls import url
from howdy import views

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),
    #url(r'^$', views.HomePageView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()), #adds the /about/ route
    #url(r'^sites/$', views.SitesPageView.as_view()), #adds the /sites/ route
]
