
from django.urls import path
# when we use . => from the internal website we are using the module
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about_us.html',views.about_us,name="about_us"),
    path('services.html',views.services,name ="services"),
    path('Industries.html',views.industries,name="industries"),
    path('packages.html',views.packages,name="packages"),
    path('latest_news.html',views.latest_news,name="latest_news"),
    path('contact-us.html',views.contact_us,name="contact-us"), 
    path('blog.html',views.blog,name="blog"),
    path('Gallery.html',views.Gallery,name ="Gallery"),
]
