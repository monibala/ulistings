from django.shortcuts import render
from Category.forms import bookingform
from home.models import order
from Category.models import  Features, List, ListCategories, MenuItems, bookedlist,  reviews, wishitems
# from django.contrib.gis.utils import GeoIP
# Create your views here.
def category(request):
    cat = ListCategories.objects.all()
    res = {'cat':cat}
    return render(request, 'category.html', res)
def listdetail(request,slug):
    category = ListCategories.objects.all()
    cat = ListCategories.objects.filter(name=slug)
    data = List.objects.filter(catgeory=slug)
    rev_rating = reviews.objects.filter(review_on=slug)
    print(data)
    res = {'data':data, 'category':category,'rev_rating':rev_rating}
    return render(request, 'listdetail.html',res)
def listingbooking(request,slug):
    if request.user.is_authenticated:
        user=request.user
        # list_bkng = request.GET.get('id')
        # print(list_bkng)
        cat = ListCategories.objects.all()
        order_data = order.objects.filter(user=user,booked_list=slug)
        # list_booked = List.objects.filter(slug=slug)
        # list_booked = List.objects.get(name=slug)
        data = List.objects.get(slug=slug)
        print(data)
        amount = 0.0
        bk = bookedlist.objects.get(listbooked=data,user=request.user)
        # bk = bookedlist.objects.get(user=user)
        # print(bk)
        # tags = ListTags.objects.all()
        # menu = MenuItems.objects.filter(restaurant=slug)
        # hours = BusinessHours.objects.filter(restaurant_name=slug)
        # feature = Features.objects.filter(hotelname=slug)
        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            mobile=request.POST['mobile']
            bookings = order(fname = fname,lname=lname,email=email,mobile=mobile,booked_list=slug)
            bookings.save()
        
        amount = int(bk.booked_price)
        print(amount)
        res= {'bk':bk,'cat':cat, 'list_booked':data,'amount':amount}
    return render(request,'listing_booking.html',res)
def wishlist(request):
    if request.user.is_authenticated:
        
        user = request.user
        listname = request.GET.get('name')
        list = List.objects.get(name = listname)
        wishitems(user=user,wish_list=list).save()
    return render(request,'wishlist.html')
def singlelist(request,slug):
    list = List.objects.all()
    rev = reviews.objects.all()
    user = request.user
    cat = ListCategories.objects.all()
    data = List.objects.get(slug=slug)
    # tags = ListTags.objects.all()
    menu = MenuItems.objects.filter(restaurant=slug)
    # hours = BusinessHours.objects.filter(restaurant_name=slug)
    feature = Features.objects.filter(hotelname=slug)
    booked_price=0.0
    # g = GeoIP() 
    # lat,lng = g.lat_lon(data.location)
    # print(lat,lng)
    if request.method=="POST":
        date =request.POST['date']
        guests = request.POST['guests']
        time =  request.POST['time']
        print(date,time)
        booked_price = data.price*int(guests)
        print(data.price)
        print(booked_price)
        bookedlist.objects.get_or_create(user=user, date=date,time=time,guests=guests,listbooked=List.objects.get(slug=slug),booked_price=booked_price)
        
    

    res = {'data':data, 'cat':cat,  'menu':menu,'list':list ,'rev':rev,'feature':feature,'booked_price':booked_price}
    return render(request, 'singlelist.html', res)
def bookingconfirm(request):
    return render(request, 'bookingconfirm.html')
def add_review(request):
    res = {}
    res['lists'] = List.objects.all()
    if request.method=="POST":
       
        rev = reviews()
        rev.name = request.POST['name']
        rev.review_on = List.objects.get(name=request.POST['review_on'])
        rev.image = request.POST.get('image')
        rev.email = request.POST['email']
        # rev.subject = request.POST['subject']
        rev.review = request.POST['review']
        rev.rating = request.POST['rating']
       
        rev.save()
    return render(request, 'review.html',res)