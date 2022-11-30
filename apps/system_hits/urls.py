from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    hits_view,
    hit_create_view,
    hit_update_failed,
    hit_update_completed,
    hits_detail,
    hits_reasign,
    page_notfound,
    page_permission_denied
)

app_name = 'system_hits'

urlpatterns = [
    path('hits/', hits_view, name='hits'),
    path('hits/<int:pk>', hits_detail, name='hits_detail'),
    path('hits/create/', hit_create_view, name='hits_create'),
    path('hits/failed/<int:pk>', hit_update_failed, name='hits_failed'),
    path('hits/completed/<int:pk>', hit_update_completed, name='hits_completed'),
    path('hits_reasign/', hits_reasign, name='hits_reasign'),
    path('page_notfound/', page_notfound, name='page_notfound'),
    path('page_permission_denied/', page_permission_denied, name='page_permission_denied')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)