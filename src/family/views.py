from django.shortcuts import render
from django.http import HttpResponse
from family.models import Contacts
from django.contrib import messages
# Create your views here.


def daughter(request, *args, **kwargs):
    print(request.user)
    print(args)
    print(kwargs)
    # return HttpResponse("<h1 >Hello Anamika</h1>")
    # Here we were returning a html txt, instead we want to use builtin django short-cut render,
    # and we can return a http template and context/data that fit with the template.

    my_context = {"about": "These are the list of names of my daughter",
                  "names":["santa_manta", "duttu_manta", "khepun_banta","duttu_banta"]}
    # In below return statement return a rendered of original request, a html template, and data that fit the
    # template
    return render(request, "daughter.html", my_context)


def myself(request, *args, **kwargs):
    print(request.user)
    print(args)
    print(kwargs)
    # return HttpResponse("<h1>Hello Swapan</h1>")
    return render(request, "swapan.html")


def wife(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    # return HttpResponse("<h1>Hello Sonai</h1>")
    context = {'about': 'There are the list of dices, can be prepared by by her',
               'dices': ['Ghugni', 'chola-dall', 'Dim-curry', 'Birianny']}
    return render(request, "wife.html", context)


def welcome(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    context = {'hello': "Welcome to swapan's family"}
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'welcome.html', context)


def home(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    # context = {'hello':'Hello World'}
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        contact = Contacts(name=name, phone=phone)
        contact.save()
        messages.success(request, 'Contact saved')
    return render(request, 'contacts.html')



