from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import room.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',room.views.first, name="first"),
    path('room/home', room.views.home, name="home"),
    path('room/register/', room.views.register, name="register"),
    path('room/newroom/',room.views.roompost, name="newroom"),
    path('room/<int:room_id>', room.views.detail, name="detail"),
<<<<<<< HEAD
    path('room/cart', room.views.cart, name="cart"),
=======
    path('room/search/', room.views.SearchFormView.as_view(), name = "search"),
>>>>>>> 5449369c2ac6500fbcf0e7e5b004cf93153ab9be
    path('create', room.views.create, name="create"),
    path('accounts/signup', accounts.views.signup, name="signup"),
    path('accounts/login', accounts.views.login, name="login"),
    path('accounts/logout', accounts.views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
