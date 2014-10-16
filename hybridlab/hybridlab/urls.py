from django.conf.urls import patterns, include, url
import chart.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^historico/$', chart.views.ListSimulationtView.as_view(), name='history'),
    url(r'^registrar/$', 'login.views.registrar', name='registrar'),
    url(r'^login/$', 'login.views.logar', name='logar'),
    # url(r'^$', 'hybridlab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
