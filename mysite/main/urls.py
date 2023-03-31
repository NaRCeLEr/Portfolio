from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('projects/', ProjectsList.as_view(), name='projects'),
    path('project/<slug:slug>', ProjectDetail.as_view(), name='project_detail'),
    path('contacts/', AddMessage.as_view(), name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
