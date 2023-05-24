from cgitb import handler
from django.urls import path, include
from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('', views.home),
    path('aboutus/', views.aboutus),
    path('whatwedo/', views.whatwedo),
    path('contact_us/', views.contact, name='contact'),
    path('alumnis/', views.alumnis),
    path('search_all/', views.search_all, name='search-all')
]

