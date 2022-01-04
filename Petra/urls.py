# we want to include or reference thar url to that in the new one
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.Urls')),
]
