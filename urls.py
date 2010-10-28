from django.conf.urls.defaults import *
from django.contrib import admin
from settings import FTP_BASE
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': FTP_BASE, 'show_indexes': True }),
)
