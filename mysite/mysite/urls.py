
from django.contrib import admin
from django.urls import path, include
from mysite import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)


