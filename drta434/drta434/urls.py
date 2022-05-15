from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from main_app.views import index
from main_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
