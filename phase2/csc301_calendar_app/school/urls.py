from django.conf.urls import patterns, include, url
from school import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csc301_calendar_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^enrol/$', views.add_school, name='Enrol in School'),
    
)
