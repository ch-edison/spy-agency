from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    login_view,
    logout_view,
    registeration_view,
    hitmen_view,
    hitmen_detail,
    hitmen_inactive,
    home_view,
    asign_hitman_to_manager
)

app_name = 'users'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registeration_view, name='registro'),
    path('hitmen/', hitmen_view, name='hitmen'),
    path('hitmen/<int:pk>', hitmen_detail, name='hitmen_detail'),
    path('hitmen/inactive/<int:pk>', hitmen_inactive, name='hitmen_inactive'),
    path('hitmen/asign_hitman_to_manager/', asign_hitman_to_manager, name='asign_hitman_to_manager'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)