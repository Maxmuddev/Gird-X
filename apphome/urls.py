from django.urls import path
from .views import *
urlpatterns = [
    path('',homeview,name = 'home'),
    path('about/',aboutview,name = 'about'),
    path('works/',worksview,name = 'works'),
    path('contact/',contactview,name = 'contact'),
]