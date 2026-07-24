from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from apps.core.admin import clinic_admin_site

urlpatterns = [
    path("django-admin/", clinic_admin_site.urls),
    path("", include("apps.core.urls")),
]

# The production deployment serves these files through Nginx.  Docker-based
# local development uses Gunicorn directly, so Django must expose the
# collected static files while DEBUG is enabled.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
