


from django.urls import path
from .views import News

urlpatterns = [
    path('', News, name= "News"),
]