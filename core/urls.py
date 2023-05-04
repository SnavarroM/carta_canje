

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('carta.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Custom titles for admin

admin.site.site_header = 'Carta de Canje'
admin.site.index_title = 'Panel de Administrador'
admin.site.site_title = 'Carta de Canje'



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)