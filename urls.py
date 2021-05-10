from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='main-home'),
    path('about/', views.about, name='about'),
    path('sell/', views.sell, name='sell'),
    path('buy/', views.buy, name='buy'),
    path('table/', views.table, name='table'),
    path('goals/', views.goals, name='goals'),
    path('partners/', views.partners, name='partners')

]
