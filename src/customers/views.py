from django.shortcuts import render, redirect, HttpResponse
from .models import Retails
from .forms import CreateRetail
from django.http import Http404
from django.contrib import messages
# Create your views here.

def customer_page(request):
    return HttpResponse("<h1> This is customer page</h1>")

def retail_customer_details(request, *args, **kwargs):
    retail_obj1 = Retails.objects.get(id=kwargs.get('id'))
    context = {"object": retail_obj1}
    return render(request, 'Retail_customer_details_template.html', context)


def retail_customers_list(request, *args, **kwargs):
    object_list = Retails.objects.all()
    context = {'items': object_list}
    return render(request, 'Retail_customers_list.html', context)


def create_retail_customer(request):
    retail_form = CreateRetail(request.POST or None)
    if retail_form.is_valid():
        retail_form.save()
    context = {'r_form': retail_form}
    return render(request, 'Retail_customer_create.html', context)


def edit_retail_customer(request, **kwargs):
    try:
        retail_obj1 = Retails.objects.get(id=kwargs.get('id'))
    except Retails.DoesNotExist:
        raise Http404
    retail_form = CreateRetail(request.POST or None, instance=retail_obj1)
    if retail_form.is_valid():
        retail_form.save()
    context = {'r_form': retail_form}
    return render(request, 'Retail_customer_create.html', context)


def delete_retail_customer(request, **kwargs):
    try:
        retail_obj1 = Retails.objects.get(id=kwargs.get('id'))
    except Retails.DoesNotExist:
        raise Http404
    context = {"object": retail_obj1}

    if request.method == "POST":
        retail_obj1.delete()
        return redirect("../")

    return render(request, 'Retail_customer_delete.html', context)

