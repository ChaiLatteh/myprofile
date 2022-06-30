from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import MenuItem


# Create your views here.
def home (request):
    return render(request, 'crave/home.html')

def menu_images(request):
    return render(request, 'crave/menu_images.html')

def menu(request):

    all_item_list=[]
    smoothie_list=[]
    special_smoothie_list=[]
    slush_list=[]
    milk_tea_list=[]
    jasmine_tea_list=[]
    special_drink_list=[]
    frappe_list=[]
    milkshake_list=[]
    waffle_list=[]
    milk_snow_list=[]
    acai_pitaya_list=[]
    cafe_list=[]
    hot_tea_list=[]
    taiyaki_list=[]
    ice_cream_list=[]

    for item in MenuItem.objects.all():
        all_item_list.append(item)

        if item.category=="smoothie":
            smoothie_list.append(item)
        if item.category=="special_smoothie":
            special_smoothie_list.append(item)
        if item.category=="slush":
            slush_list.append(item)
        if item.category=="milk_tea":
            milk_tea_list.append(item)
        if item.category=="jasmine_tea":
            jasmine_tea_list.append(item)
        if item.category=="special_drink":
            special_drink_list.append(item)
        if item.category=="frappe":
            frappe_list.append(item)
        if item.category=="milkshake":
            milkshake_list.append(item)
        if item.category=="waffle":
            waffle_list.append(item)
        if item.category=="milk_snow":
            milk_snow_list.append(item)
        if item.category=="acai_pitaya":
            acai_pitaya_list.append(item)
        if item.category=="cafe":
            cafe_list.append(item)
        if item.category=="hot_tea":
            hot_tea_list.append(item)
        if item.category=="taiyaki":
            taiyaki_list.append(item)
        if item.category=="ice_cream":
            ice_cream_list.append(item)

    data = {
    "all_item_list": all_item_list,

    "smoothie_list": smoothie_list,
    "special_smoothie_list": special_smoothie_list,
    "special_drink_list": special_drink_list,
    "slush_list": slush_list,
    "milk_tea_list": milk_tea_list,
    "jasmine_tea_list": jasmine_tea_list,
    "frappe_list": frappe_list,
    "milkshake_list": milkshake_list,
    "waffle_list": waffle_list,
    "milk_snow_list": milk_snow_list,
    "acai_pitaya_list": acai_pitaya_list,
    "cafe_list": cafe_list,
    "hot_tea_list": hot_tea_list,
    "ice_cream_list": ice_cream_list,
    "taiyaki_list": taiyaki_list,
    }

    return render(request, 'crave/menu.html', data)

def about_us(request):
    return render(request, 'crave/about_us.html')

def contact_us(request):
    return render(request, 'crave/contact_us.html')

def careers(request):
    return render(request, 'crave/careers.html')
