from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from product.models import Event, Programs, News, ProductsCategory
from .forms import ContactForm, InvolvedForm
from django.contrib import messages

from .models import Team, Partners, Statitics, Alumnis

# Create your views here.

def search_all(request):
    if request.method == "POST":
        searched = request.POST['searched']
        news = News.objects.filter(title__contains=searched)
        events = Event.objects.filter(title__contains=searched)
        programs = Programs.objects.filter(title__contains=searched)

        total = []
        for i in news:
            total.append(i)
        
        for i in events:
            total.append(i)
        
        for i in programs:
            total.append(i)

        print(total)
    
        say = News.objects.filter(title__contains=searched).count() + Event.objects.filter(title__contains=searched).count() + Programs.objects.filter(title__contains=searched).count()

        if say == 0:
            ok = 'No results were found for your search...'
            return render(request, 'search.html', {'searched':searched, 'ok':ok})


        return render(request, 'search.html', {'searched':searched, 'total':total})
    else:
        return render(request, 'search.html')


def error_404(request, exception):
    return render(request, 'error.html')

def home(request):
    statitics = Statitics.objects.all()

    form = InvolvedForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = InvolvedForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            # submitted = True
            return HttpResponseRedirect('/')
        else:
            # form = ContactForm()
            # submitted = True
            print('Form is invalid')


    partners = Partners.objects.all().order_by('-id')
    products = ProductsCategory.objects.all().order_by('-id')[0:][:3]
    programs = Programs.objects.filter(is_published = True).order_by('-id')[0:][:3]
    upcoming1 = Event.objects.filter(is_published = True).order_by('-id')[:1]
    upcoming3 = Event.objects.filter(is_published = True).order_by('-id')[1:] [:3]
    context = {
        'upcoming1' : upcoming1,
        'upcoming3' : upcoming3,
        'form':form,
        'partners' : partners,
        'statitics' : statitics,
        'programs' : programs,
        'products' : products
    }

    return render(request, 'index.html', context)


def aboutus(request):
    team = Team.objects.all().order_by('-id')
    alumnis = Alumnis.objects.all().order_by('-id')

    context = {
        'alumnis' : alumnis,
        'team' : team
    }

    return render(request, 'aboutus.html', context)


def whatwedo(request):
    return render(request, 'whatwedo.html')

def alumnis(request):
    alumnis = Alumnis.objects.all().order_by('-id')
    context = {
        'alumnis' : alumnis,
    }
    return render(request, 'alumnis.html', context)


def contact(request):
    submitted = False

    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            print('Form save')
            # submitted = True
            return HttpResponseRedirect('/contact_us/')
        else:
            # form = ContactForm()
            # submitted = True
            print('Form is invalid')
    context = { 
        'form':form
    }
    return render(request, 'contact.html', context)