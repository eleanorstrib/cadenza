from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^motif/', include('motif.urls')),
    url(r'^admin/', admin.site.urls),
]
