from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from accounts import urls as cuentasUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^posts/new/$', views.UpdateView.as_view(), name="new"),
     url(r'^posts/$', views.ListView.as_view(), name = "losPosts"),
     url(r'^posts/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
     url(r'^',include(cuentasUrls))

]
