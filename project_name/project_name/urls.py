from django.conf.urls import patterns, include, url
from django.contrib import admin
from payments import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^admin/', include(admin.site.urls)),
)
