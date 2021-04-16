from django.urls import path, include
from .views import IndexView as message


urlpatterns = [
    path('message/', message.message, name='message'),
    path('message/<slug>', message.sinmessage, name='singlemessage'),
]
