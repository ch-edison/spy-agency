from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.users.urls', namespace="users")),
    path('', include('apps.system_hits.urls', namespace="system_hits")),
]

handler404 = 'apps.system_hits.views.page_notfound'
handler403 = 'apps.system_hits.views.page_permission_denied'