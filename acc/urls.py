from django.urls import path
from . import views

# home view
urlpatterns = [
    # form route
    path('', views.home_page, name='home_page'),

]