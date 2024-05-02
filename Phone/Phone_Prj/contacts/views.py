from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, RedirectView, CreateView
from .models import Phone

# Create your views here.
'''
class IndexView(ListView):         
    #model = Phone                          
    template_name = 'contacts/index.html'      
    context_object_name = 'phones'             
    queryset = Phone.objects.all().order_by('name')
'''

def index(request):
    phones = Phone.objects.all().order_by('name')
    return render(request,"contacts/index.html", {'phones':phones})


def result(request):
    search_keyword = request.GET.get('data')
    search_list = Phone.objects.filter(name__contains = search_keyword).order_by('name')

    return render(request, "contacts/result.html", {'result': search_list, 'data':search_keyword})


def list(requset):
    phones = Phone.objects.all().order_by('name')
    return render(requset,"contacts/list.html", {'phones':phones})


def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')
        
        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email,
        )
        return redirect('list')
    return render(request, 'contacts/create.html')


def detail(request, id):
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'contacts/detail.html', {'phone':phone})

def update(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.name = request.POST.get('name')
        phone.phone_num = request.POST.get('phone_num')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('detail', id)
    return render(request, 'contacts/update.html', {'phone':phone})

def delete(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.delete()
        return redirect('list')
    return render(request, 'contacts/delete.html', {'phone': phone})




