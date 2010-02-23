from django.conf.urls.defaults import *
from Passwords.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^passApp/$', testDisplay),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^passApp/admin/(.*)', admin.site.root),
     (r'^passApp/accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
