from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showBooks, name="index"),
    path('contact', views.contactView, name='contact'),
    path('<str:user_language>', views.set_language_from_url, name='set_language_from_url'),
]



