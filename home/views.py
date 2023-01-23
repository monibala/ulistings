from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from home.forms import NewUserForm
from django.contrib.auth import logout
from Category.models import List, ListCategories
from Blog.models import bloginfo
from django.db.models import Count
from home.models import contact_info
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.
def index(request):
    res = {}
    res['list'] = List.objects.all()
    res['listcat'] = ListCategories.objects.all()
    res['blg'] = bloginfo.objects.all()
    res['count_list'] = List.objects.values('catgeory').annotate(category_count=Count('catgeory')).order_by()
    # print(count_list)
    return render(request, 'index.html', res)
def login_user(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            print('welcome')
            messages.success(request, f' welcome {username} !!')
            
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist plz sign in')
    form = AuthenticationForm()
    return redirect('index')
def register(request):
    if request.method=="POST":
        print('registered')
        form = NewUserForm(request.POST)
        if form.is_valid:
            form.save()
            
            messages.success(request, "Registration successful." )
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return redirect('index')
    
def logout_view(request):
    logout(request)
    return redirect('index')

def about(request):
    return render (request, 'about.html')
def contact(request):
    if request.method=="POST":

        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        subject = request.POST['subject']
        email = request.POST['email']
        text = request.POST['text']
        con =contact_info(name=name,mobile_number=mobile_number,subject=subject,email=email,text=text)
        con.save()
        msg1=(f'\n\n\n Name :  {name} \n Email :  {email} \n Subject : {subject} \n  Message :  {text}')
            
        send_mail(subject,msg1,email,[settings.EMAIL_HOST_USER],fail_silently=False)
        messages.success(request,'Your Message Send Successfully.')
    return render (request, 'contact.html')
def search(request):
    category = ListCategories.objects.all()
    data =List.objects.all()
    if request.method == 'GET':
        query = request.GET.get('search')
        print(query)
        if query:
            
            querydata = List.objects.filter(name__icontains=query)
            print(querydata)
            return render(request,'listdetail.html',{'querydata':querydata, 'category':category, 'data':data})
        else:
            print('No information available!!')
            return redirect('index')
    # return render(request,'searchmap.html')