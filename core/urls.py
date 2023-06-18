from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # add this
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("page-404/", TemplateView.as_view(template_name='home/../apps/templates/page-404.html'), name='page_404'),
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.home.urls")),  # UI Kits Html files
    path("settings/", include("apps.settings.urls")),  # UI Kits Html files
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
