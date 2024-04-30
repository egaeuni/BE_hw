from django.shortcuts import render
from django.views.generic import ListView
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

def index(request):
    phones = Phone.objects.all().order_by('name')
    return render(request,"contacts/index.html", {'phones':phones})
