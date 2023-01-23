from django.shortcuts import render

from Blog.models import bloginfo

# Create your views here.
def blog(request):
    res= {}
    res['bl'] = bloginfo.objects.all()
    return render(request, 'blog.html', res)
def blogdetail(request,slug):
    data = bloginfo.objects.get(slug=slug)
    res = {'data':data}
    return render(request, 'blogdetail.html',res)