from django.urls import path
from . import views

# Defined urls
urlpatterns = [
    path('', views.home, name='home'),
    path('timeline/', views.timeline, name='timeline'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_comment/<int:race_id>/', views.add_comment, name='add_comment'),
    path('add_race/', views.add_race, name='add_race'),
]
