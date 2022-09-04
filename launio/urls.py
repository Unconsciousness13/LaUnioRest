from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('launio.club.urls')),
                  path('api/', include('launio.api.urls')),
                  path('accounts/', include('launio.accounts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'launio.accounts.views.handler404'
handler500 = 'launio.accounts.views.handler500'
