from django.conf.urls import include, url
from django.contrib import admin
#from . import views

urlpatterns = [
	url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),

]
