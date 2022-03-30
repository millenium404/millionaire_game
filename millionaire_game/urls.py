from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('game/', include('game.urls')),
    path('account/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
