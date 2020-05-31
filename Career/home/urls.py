from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('top/', views.top, name='top'),
    path('after10/', views.after10, name='after10'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('reg/', views.reg, name='reg'),
    path('counselling/', views.counselling, name='counselling'),
    path('trusts/', views.trusts, name='trusts'),
    path('scholar/', views.scholar, name='scholar'),
    path('login/', views.login, name='login'),
    # url(r'^register/$', views.user_register, name='user_register')
]
