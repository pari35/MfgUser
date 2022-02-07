

from django.conf import Settings
from django.contrib import admin
from django.urls import path
from management import views

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-user/',views.add_user,name="add_user"),
    path('search/',views.search,name="search"),
    path('user-management/',views.user_management,name="user_management"),
    path('edit_user/',views.update_user, name="edit_user"),
    path('register/',views.user_register, name="admin_register"),
    path('login/',views.loginn, name="login"),
    path('update-user/',views.update_user_DB, name="update_user_DB"),
    path('sites/',views.sites, name="sites"),
]
# +static(settings.MEDIA_URL, document_root=Settings.MEDIA_ROOT)
