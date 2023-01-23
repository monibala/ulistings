from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.dashboard, name='dashboard'),
    path('ad_login',views.ad_login, name='ad_login'),
    path('ad_register', views.ad_register, name='ad_register'),
    path('ad_logout', views.ad_logout, name='ad_logout'),
    path('ad_list', views.ad_list,name='ad_list'),
    path('addlist', views.addlist, name='addlist'),
    path('ad_features', views.ad_features, name='ad_features'),
    path('addfeature',views.addfeatures, name='addfeatures'),
    path('addlistcategory',views.addlistcategory, name='addlistcategory'),
    path('ad_listcategories',views.ad_listcategories, name='ad_listcategories'),
    path('addmenu',views.addmenu, name='addmenu'),
    path('ad_menu',views.ad_menu, name='ad_menu'),
    path('addblog',views.addblog, name='addblog'),
    path('ad_blog',views.ad_blog, name='ad_blog'),
    path('addlisting/', views.addlisting, name='addlisting'),
    path('mylisting/', views.mylisting, name='mylisting'),
    path('dashboardbookings/', views.dashboardbookings, name='dashboardbookings'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('ad_reviews/', views.ad_reviews, name='ad_reviews'),
]