#   Dajngo
from django.urls import path
from online_store_app import views

urlpatterns = [
        #   urls site 
    path('', views.home, name = 'home'),
    path('store', views.store, name = 'store'),
]