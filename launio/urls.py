from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
                  path('admin/', admin.site.urls),
                #   path('', include('launio.club.urls')),
                  path ('', TemplateView.as_view(template_name='index.html')),
                  path('api/', include('launio.api.urls')),
                  path('accounts/', include('launio.accounts.urls')),
                  
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'launio.accounts.views.handler404'
handler500 = 'launio.accounts.views.handler500'
