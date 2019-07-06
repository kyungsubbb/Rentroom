from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import room.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', room.views.home, name="home"),
    path('room/register/', room.views.register, name="register"),
    path('room/<int:room_id>', room.views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
