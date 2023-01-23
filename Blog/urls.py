from django.urls import path
from  . import views
urlpatterns = [ 
    path('blog/', views.blog, name='blog'),
    path('blogdetail/<slug:slug>', views.blogdetail, name='blogdetail'),
]