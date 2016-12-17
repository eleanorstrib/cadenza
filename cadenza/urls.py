from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('signup.urls')),
    url(r'^motif/', include('motif.urls')),
]
