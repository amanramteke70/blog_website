from django.shortcuts import render, HttpResponse
from App.models import Contact
from App.models import Blognews
from django.shortcuts import redirect
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    blogsdata = Blognews.objects.all()
    paginator = Paginator(blogsdata,3)
    page_number = request.GET.get("page")
    blogsdatafinal = paginator.get_page(page_number)
    totalpage = blogsdatafinal.paginator.num_pages

    data = {
        'blogsdata': blogsdatafinal,
        'totalpage' : totalpage,
        'totalfinalpage': [n+1 for n in range(totalpage)],
        }
    
    return render(request,'index.html', data)
    
def about(request):
    return render(request,'about.html')
    
def contact(request):

    emp = Contact.objects.all()  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        emp = Contact(
        name = name,
        phone = phone,
        email = email,
        message = message
    )
        emp.save()
        
    return render(request, 'contact.html')

def blogDetails(request, slug):
    newdetails = Blognews.objects.filter(slug=slug).first()
    data = {
        'newdetails':newdetails
    }
    return render(request, 'video-page.html', data)

def search(request):

    blogsdata = Blognews.objects.all()
    
    if request.method == 'GET':
        st = request.GET.get('search')
        if st!=None:
            blogsdata = Blognews.objects.filter(tittle__icontains=st)

    params = {
        'blogsdata': blogsdata
    }
    return render(request, 'search.html', params)