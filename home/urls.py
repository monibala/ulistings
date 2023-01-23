from django.urls import path
from  . import views
urlpatterns = [ 
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search-query/', views.search, name='search'),
]