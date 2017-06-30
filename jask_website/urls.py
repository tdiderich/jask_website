from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^$', views.home, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
