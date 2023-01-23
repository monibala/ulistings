from django.shortcuts import render,redirect
from Superuser.dashboardsettings import getmodelbyappname, getObjectbyAppModelName, hiddenFieldInAdminAllModel
from Superuser.forms import GenForm
from django.contrib import messages
from django.contrib import messages as sms
from django.core.paginator import Paginator
from Category.models import Features, List, ListCategories, MenuItems, reviews
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from Superuser.models import ad_profile
from django.contrib.auth.models import User
from home.forms import NewUserForm
from Blog.models import bloginfo
# Create your views here.
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res = {}
        res['dashboardheading'] = 'Dashboard'
        # for data in res['modelslist']:
        #     print(res['modelslist'][data])
        #     break
        # for app in allapps:
        #     res.append({app:apps.all_models[app]})
        return render(request,'superuser/dashboard.html',res)
    else:
        return redirect('ad_login')
def ad_register(request):
    if request.method=="POST":
        print('registered')
        form = NewUserForm(request.POST)
        if form.is_valid:
            form.save()
            
            messages.success(request, "Registration successful." )
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return redirect('dashboard')
def ad_login(request):
    
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            print('welcome')
            messages.success(request, f' welcome {username} !!')
            
            return redirect('dashboard')
        else:
            messages.info(request, f'Account does not exist plz sign in')
    form = AuthenticationForm()
    return render(request,'superuser/login.html')
def ad_logout(request):
    logout(request)
    return redirect('ad_login')
# add list
def addlist(request):
    
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['cat']=ListCategories.objects.all()
        print(res)
        if request.method=='POST' :
            print('form')
            catgeory=ListCategories.objects.get(name=request.POST['catgeory'])
            name=request.POST['name'] 
            images=request.POST['images']
            description=request.POST['description']
            mobile=request.POST['mobile'] 
            email=request.POST['email']
            website=request.POST['website']
            address=request.POST['address']
            location=request.POST['location']
            price=request.POST['price']
            contact_person=request.POST['contact_person']
            contact_photo=request.POST['contact_photo']   
        
            # try:
            list= List(catgeory=catgeory,name=name,images=images,description=description,mobile=mobile,email=email,website=website,address=address,location=location,contact_person=contact_person,contact_photo=contact_photo,price=price)
            list.save()
            sms.success(request,'List Added.')
            return redirect('ad_list')
            # except Exception as p:
            #     sms.warning(request,'All Field Are Required !')
            #     return redirect('addlist')

    
        return render(request,'superuser/dashboard_add_listing.html',res)
    else:
        return redirect('dashboard')
        # Edit delete
def ad_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['lists']=List.objects.all()
        res['cat'] = ListCategories.objects.all()
        
        # paginator=Paginator(res['lists'],6)
        # page_no=request.GET.get('page')
        # res['list']=paginator.get_page(page_no)
        # res['tot']=len(res['lists'])
        # nxt=request.get_full_path()
        if request.method=='POST':
            if request.POST.get('listid')!=None: # for edit
                print('listid')
                if request.POST.get('catgeory')!=None:
                    catgeory=ListCategories.objects.filter(name=request.POST.get('catgeory'))
                name=request.POST['name'] 
                images=request.POST['images']
                description=request.POST['description']
                location = request.POST['location']
                mobile=request.POST['mobile'] 
                email=request.POST['email']
                website=request.POST['website']
                address=request.POST['address']
                price=request.POST['price']
                contact_person=request.POST['contact_person']
                contact_photo=request.POST['contact_photo']
                editlist= List.objects.filter(name=request.POST['listid'])
                if len(editlist)>0:
                    ob=editlist[0]
                    if request.POST.get('catgeory')!=None and len(catgeory)>0:
                        ob.catgeory=ListCategories.objects.get(name=request.POST.get('catgeory'))
                    if len(name)>0:
                        ob.name=name
                    if len(images)>0:
                        ob.images=images
                    if len(description)>0:
                        ob.description=description
                    if len(mobile)>0:
                        ob.mobile=mobile
                    if len(email)>0:
                        ob.email = email
                    if len(website)>0:
                        ob.website=website
                    if len(price)>0:
                        ob.price=price
                    if len(address)>0:
                        ob.address=address 
                    if len(location)>0:
                        ob.location=location   
                    if len(contact_person)>0:
                        ob.contact_person=contact_person
                    if len(contact_photo)>0:
                        ob.contact_photo=contact_photo
                    ob.save()
                    sms.success(request,'List Updated.')
                # return redirect(nxt)
            elif request.POST.get('name')!=None: # for delete
                listid=request.POST['name']
                print(listid)
                li=List.objects.filter(name=listid)
                print(li)
                li.delete()
                sms.success(request,'Product Deleted SuccessFully.')
                    # return redirect(nxt)    
           
        return render(request,'superuser/dashboard_my_listing.html',res)
    else:
        return redirect('index')
def ad_features(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['features']=Features.objects.all()
        # paginator=Paginator(res['features'],6)
        # page_no=request.GET.get('page')
        # res['features']=paginator.get_page(page_no)
        # res['tot']=len(res['features'])
        res['list'] = List.objects.all()
        # nxt=request.get_full_path()
        if request.method=="POST":
            if request.POST.get('featureid')!=None: # for edit
                
                features_list=request.POST['features_list']
                if request.POST.get('hotelname')!=None:
                    hotelname=List.objects.filter(name=request.POST.get('hotelname'))
                
                feature= Features.objects.filter(id=request.POST['featureid'])
                if len(feature)>0:
                    ob=feature[0]
                    if len(features_list)>0:
                        ob.features_list=features_list
                    if request.POST.get('hotelname')!=None and len(hotelname)>0:
                        ob.hotelname=List.objects.get(name=request.POST.get('hotelname'))
                    ob.save()
                    sms.success(request,'Features Updated.')
                    # return redirect(nxt)    

        elif request.POST.get('fid')!=None: # for delete
                featureid=request.POST['fid']
                feature=Features.objects.filter(id=featureid)
                feature.delete()
                sms.success(request,'Feature Deleted SuccessFully.')
                # return redirect(nxt)           
        return render(request,'superuser/dashboard_my_listing.html',res)
    else:
        return redirect('index')
def addfeatures(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['list'] = List.objects.all()
        if request.method=='POST':
            features_list = request.POST['features_list']
            hotelname = List.objects.get(name=request.POST['hotelname'])
            feature = Features(features_list=features_list,hotelname=hotelname)
            feature.save()
            sms.success(request,'List Added.')
            return redirect('ad_features')
        return render(request,'superuser/addfeature.html',res)
    else:
        return redirect('ad_login')
def addlistcategory(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['listcategory'] = ListCategories.objects.all()
        if request.method=='POST':
            name = request.POST['name']
            icon = request.POST['icon']
            listcategory = ListCategories(name=name,icon=icon)
            listcategory.save()
            sms.success(request,'ListCategory Added.')
            return redirect('ad_listcategories')
        return render(request,'superuser/addlistcategory.html',res)
    else:
        return redirect('ad_login')

def ad_listcategories(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['list_category']=List.objects.all()
        res['category'] = ListCategories.objects.all()
        # paginator=Paginator(res['list_category'],6)
        # page_no=request.GET.get('page')
        # res['list_category']=paginator.get_page(page_no)
        # res['tot']=len(res['list_category'])
        # nxt=request.get_full_path()
        if request.method=='POST':
            if  request.POST.get('listcatid')!=None: # for edit
                name=request.POST['name']
                icon=request.POST['icon'] 
                
                list_category= ListCategories.objects.filter(name=request.POST['listcatid'])
                if len(list_category)>0:
                    ob=list_category[0]
                    if len(name)>0:
                        ob.name=name
                    if len(icon)>0:
                        ob.icon=icon
                    ob.save()
                    sms.success(request,'Category Updated.')
                    # return redirect(nxt)    
                
                # return render(request,'superuser/dashboard_my_listing.html',res)
            elif request.POST.get('catid')!=None: # for delete
                catid=request.POST['catid']
                list_category=ListCategories.objects.filter(name=catid)
                list_category.delete()
                sms.success(request,'Category Deleted SuccessFully.')
                # return redirect(nxt)
        return render(request,'superuser/dashboard_my_listing.html',res)
    else:
        return redirect('index')
def addmenu(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['list'] = List.objects.all()
        res['menu'] = MenuItems.objects.all()
        if request.method=='POST':
            menutags=request.POST['menutags']
            items=request.POST['items'] 
            restaurant = List.objects.get(name=request.POST['restaurant'])
            price = request.POST['price']
            menu = MenuItems(menutags=menutags,items=items,restaurant=restaurant,price=price)
            menu.save()
            sms.success(request,'Menu Added.')
            return redirect('ad_menu')
        return render(request,'superuser/addmenu.html',res)
    else:
        return redirect('ad_login')
def ad_menu(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['list'] = List.objects.all
        res['menu'] = MenuItems.objects.all()
        # paginator=Paginator(res['menu'],6)
        # page_no=request.GET.get('page')
        # res['menu']=paginator.get_page(page_no)
        # res['tot']=len(res['menu'])
        # nxt=request.get_full_path()
        if request.method=='POST':
            if request.POST.get('menuid')!=None: # for edit
                menutags=request.POST['menutags']
                items=request.POST['items'] 
                restaurant = List.objects.get(name=request.POST['restaurant'])
                price = request.POST['price']
                menu=MenuItems.objects.filter(items=request.POST['menuid'])
                if len(menu)>0:
                    ob=menu[0]
                    if len(menutags)>0:
                        ob.menutags=menutags
                    if len(items)>0:
                        ob.items=items
                    # if len(restaurant)>0:
                    #     ob.restaurant=restaurant
                    if request.POST.get('restaurant')!=None:
                        ob.restaurant=List.objects.get(name=request.POST.get('restaurant'))
                    if len(price)>0:
                        ob.price=price 
                    ob.save()
                    sms.success(request,'Menu Updated.')
                    # return redirect(nxt)    
           
                # return render(request,'superuser/dashboard_my_listing.html',res)
            elif request.POST.get('menuitemid')!=None: # for delete
                menuitemid=request.POST['menuitemid']
                menu=MenuItems.objects.filter(items=menuitemid)
                menu.delete()
                sms.success(request,'Menu Deleted SuccessFully.')
                # return redirect(nxt)
        return render(request,'superuser/dashboard_my_listing.html',res)
    else:
        return redirect('ad_login')
def addblog(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['blg'] = bloginfo.objects.all()
        
        if request.method=='POST':
            title=request.POST['title']
            images=request.POST['images'] 
            description = request.POST['description']
            posted_by = request.POST['posted_by']
            date = request.POST['date']
            blg = bloginfo(title=title,images=images,description=description,posted_by=posted_by,date=date)
            blg.save()
            sms.success(request,'Blog Added.')
            return redirect('ad_blog')
        return render(request,'superuser/addblog.html',res)
    else:
        return redirect('ad_login')
def ad_blog(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['blg'] = bloginfo.objects.all
        
        # paginator=Paginator(res['menu'],6)
        # page_no=request.GET.get('page')
        # res['menu']=paginator.get_page(page_no)
        # res['tot']=len(res['menu'])
        # nxt=request.get_full_path()
        if request.method=='POST':
            if request.POST.get('blogid')!=None: # for edit
                title=request.POST['title']
                images=request.POST['images'] 
                description = request.POST['description']
                posted_by = request.POST['posted_by']
                date = request.POST['date']
                blg=bloginfo.objects.filter(title=request.POST['blogid'])
                if len(blg)>0:
                    ob=blg[0]
                    if len(title)>0:
                        ob.title=title
                    if len(images)>0:
                        ob.images=images
                    if len(description)>0:
                        ob.description=description
                    
                    if len(posted_by)>0:
                        ob.posted_by=posted_by 
                    if len(date)>0:
                        ob.date=date 
                    ob.save()
                    sms.success(request,'Blog Updated.')
                    # return redirect(nxt)    
           
                # return render(request,'superuser/dashboard_my_listing.html',res)
            elif request.POST.get('title')!=None: # for delete
                title=request.POST['title']
                blg=bloginfo.objects.filter(title=title)
                blg.delete()
                sms.success(request,'Blog Deleted SuccessFully.')
                # return redirect(nxt)
        return render(request,'superuser/dashboard_my_listing.html',res)
    else:
        return redirect('ad_login')

def addlisting(request):
    return render(request, 'superuser/dashboard_add_listing.html')
def mylisting(request):
    return render(request, 'superuser/dashboard_my_listing.html')
def dashboardbookings(request):
    return render (request, 'superuser/dashboard_bookings.html')
def profile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['profile']=ad_profile.objects.filter(user=request.user)
        if request.method=='POST':
            
            email=request.POST['email']
            name=request.POST['name']
            img=request.POST['img']
            dob=request.POST['dob']
            address=request.POST['address']
            about=request.POST['about'] 
            mobile=request.POST['mobile']
            designation = request.POST['designation']
            pro= ad_profile.objects.filter(user=request.user)
            if len(pro)>0:
                ob=pro[0]
                ob.user=User.objects.get(id=request.user.id)
                if len(name)>0:
                    ob.name=name
                if len(img)>0:
                    ob.img=img
                if len(email)>0:
                    ob.email=email
                if len(dob)>0:
                    ob.dob=dob
                if len(mobile)>0:
                    ob.mobile=mobile
                if len(about)>0:
                    ob.about=about
                if len(address)>0:
                    ob.address=address
                if len(designation)>0:
                    ob.designation=designation
                ob.save()
                sms.success(request,'Profile Updated.')
                return redirect('profile')
            # else:
            #         try:
            #             ad_profile(user=User.objects.get(id=request.user.id),name=name,img=img,email=email,dob=dob
            #             ,mobile=mobile,about=about,address=address,designation=designation).save()
            #             sms.success(request,'Profile Updated.')
            #             return redirect('ad_profile')
            #         except Exception as e:
            #             res['error']='All Field Required !'
            #             return render(request,'superuser/dashboard_my_profile.html',res)
    return render(request, 'superuser/dashboard_my_profile.html',res)
def changepassword(request):
    user = request.user
    if request.method=="POST":
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        if newpassword==confirmpassword:
            user.set_password('newpassword')
            user.save()
        else:
            print('Password not matched')

    return render(request, 'superuser/dashboard_change_password.html')
def ad_reviews(request):
    res={}
    res['rev'] = reviews.objects.all()
    return render(request, 'superuser/dashboard_visitor_review.html', res)