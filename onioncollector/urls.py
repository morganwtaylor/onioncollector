
from django.contrib import admin
from django.urls import path, include

from links import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('links/', include('links.urls', namespace='links')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', views.home, name='home'),
]
