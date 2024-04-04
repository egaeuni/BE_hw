from django.shortcuts import render
from .models import Phone

# Create your views here.
def index(request):
    phones = Phone.objects.all().order_by('name')
    return render(request,"contacts/index.html", {'phones':phones})

def result(request):
    search_keyword = request.GET.get('data')
    search_list = Phone.objects.filter(name__contains = search_keyword).order_by('name')

    return render(request, "contacts/result.html", {'result': search_list, 'data':search_keyword})