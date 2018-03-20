from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views
from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [

    url('stocks/', views.stoList),
    url('upload', views.fileUpload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
