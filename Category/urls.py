from django.urls import path
from . import views
urlpatterns = [
    path('category/', views.category, name='category'),
    path('listdetail/<slug:slug>', views.listdetail, name='listdetail'),
    path('listingbooking/<slug>/', views.listingbooking, name='listingbooking'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('singlelist/<slug:slug>', views.singlelist, name='singlelist'),
    path('review/', views.add_review, name='review'),
    path('bookingconfirm/', views.bookingconfirm, name='bookingconfirm'),
    ]