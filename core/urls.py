from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.IndexTemplateView.as_view(), name="index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
