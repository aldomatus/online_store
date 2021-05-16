#   Dajngo
from django.urls import path
from online_store_app import views

urlpatterns = [
        #   urls site 
    path('', views.home, name = 'home'),
    path('services', views.services, name = 'services'),
    path('store', views.store, name = 'store'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
]