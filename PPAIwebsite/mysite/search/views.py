from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponse, render

from wagtail.models import Page
from wagtail.search.models import Query

from django.shortcuts import render, redirect
from home.models import Values
from django.contrib import messages
from datetime import datetime


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )

# Create your views here.
def index(request):
    return render(request,'search/index.html')

def index1(request):
    return render(request,'search/index1.html')

def membership(request):
    return render(request,'search/membership.html')

def membership1(request):
    return render(request,'search/membership1.html')

def downloads(request):
    return render(request,'search/downloads.html')

def downloads1(request):
    return render(request,'search/downloads1.html')

def conferences(request):
    return render(request,'search/conferences.html')

def conferences1(request):
    return render(request,'search/conferences1.html')

def awards(request):
    return render(request,'search/awards.html')

def awards1(request):
    return render(request,'search/awards1.html')

def registration11(request):
    return render(request,'search/registration11.html')

def registration12(request): #new
    return render(request,'search/registration12.html')

def registration01(request):
    return render(request,'search/registration01.html')

def registration02(request): #new
    return render(request,'search/registration02.html')

def InsertValue(request):
    mydate = datetime.now().date()
    if(request.method=='POST'):
        if(request.POST.get('username') and request.POST.get('password')):
            result = Values.objects.filter(username=request.POST.get('username'))
            if(len(result)>0):
                messages.error(request, 'This username already exists')
                return render(request, 'search/registration.html')
            else:
                saverecord = Values()
                saverecord.date = mydate
                saverecord.username = request.POST.get('username')
                saverecord.password = request.POST.get('password')
                saverecord.membership = request.POST.get('membership')
                saverecord.save()
                return render(request, 'search/login.html')
    else:
        return render(request, 'search/index.html')

def welcome(request):
    return render(request, 'search/index.html')

def login(request):
    return render(request, 'search/login.html')

def register(request):
    return render(request, 'search/myregistration.html')

def index1(request):
    return render(request, 'search/index1.html')

def index(request):
    return render(request, 'search/index.html')



def ShowValues(request):
    if(request.method=='POST'):
        if(request.POST.get('username') and request.POST.get('password')):
            result = Values.objects.filter(username=request.POST.get('username'))
            if(len(result)==0):
                messages.error(request, 'Invalid credentials')
                return render(request, 'search/login.html')
            else:
                for i in result:
                    if(i.username == request.POST.get('username') and i.password== request.POST.get('password')):
                        d1 = datetime.strptime(i.date, "%Y-%m-%d")
                        d2 = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")
                        diff = int((d2-d1).days)
                        # diff = datetime.now().date()-i.date
                        if(i.membership=="annual" and diff<=365):
                            return render(request, 'search/index1.html', {'name':request.POST.get('username')})
                        elif(i.membership=="annual" and diff>365):
                            messages.error(request, 'Your membership time has finished. Please renew')
                            return render(request, 'search/login.html')
                        elif(i.membership=="lifetime"):
                            return render(request, 'search/index1.html', {'name':request.POST.get('username')})
                    else:
                        messages.error(request, 'Invalid credentials')
                        return render(request, 'search/login.html')
        else:
            return render(request, 'search/myindex.html')

    else:
        return render(request, 'search/myindex.html')



