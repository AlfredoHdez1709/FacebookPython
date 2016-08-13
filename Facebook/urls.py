from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from accounts import urls as cuentasUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^posts/$', views.UpdateView.as_view(), name="nuevo"),
     #url(r'^blog/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
     url(r'^',include(cuentasUrls))

]
