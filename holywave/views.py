from django.shortcuts import render, redirect

from django.core.paginator import Paginator
import collections
from datetime import datetime, date
from .models import Leader, UpcomingEvent, UpcomingClass, UpcomingEventDraft, UpcomingClassDraft, Sermon, MinistryCategory, Ministry, Reading, Button

# Create your views here.
def home(request):
    upcomingevents_list = []
    upcomingclasses_list = []
    for upcomingevent in UpcomingEvent.objects.all().order_by("start_date", 'end_date'):
        if upcomingevent.end_date >= datetime.today().date():
            upcomingevents_list.append(upcomingevent)
    for upcomingclass in UpcomingClass.objects.all().order_by("start_date", 'end_date'):
        if upcomingclass.end_date >= datetime.today().date():
            upcomingclasses_list.append(upcomingclass)



    data = {
    "upcomingevents_list":upcomingevents_list,
    "upcomingclasses_list":upcomingclasses_list,
    }



    return render(request, 'holywave/home.html', data)

def about(request):
    return render(request, 'holywave/about/about.html')

# def who_we_are(request):
#     return render(request, 'holywave/about/who_we_are.html')

def our_story(request):
    return render(request, 'holywave/about/our_story.html')

def leadership(request):
    if request.method == "GET":
        all_leaders_list=[]

        for leader in Leader.objects.all().order_by("sort_title", "hierarchy", "first_name"):
            if leader.active:
                all_leaders_list.append(leader)
        data={
        "leaders_list": all_leaders_list,
        }

    return render(request, 'holywave/about/leadership.html', data)

def leadership_filter(request):
    if request.POST['title']=="All Leaders":
        return redirect('/holywave/about/leadership')
        # for leader in Leader.objects.all().order_by('first_name'):
        #     filtered_leaders.append(leader)

    elif request.POST['title']=="Pastors":
        return redirect('/holywave/about/leadership/pastors')
        # for leader in Leader.objects.filter(title="pastors").order_by('first_name'):
        #     filtered_leaders.append(leader)

    elif request.POST['title']=="Elders":
        return redirect('/holywave/about/leadership/elders')
        # for leader in Leader.objects.filter(title="elders").order_by('first_name'):
        #     filtered_leaders.append(leader)

    elif request.POST['title']=="Deacons":
        return redirect('/holywave/about/leadership/deacons')
        # for leader in Leader.objects.filter(title="deacons").order_by('first_name'):
        #     filtered_leaders.append(leader)

    elif request.POST['title']=="Ministry Leaders":
        return redirect('/holywave/about/leadership/ministry_leaders')
        # for leader in Leader.objects.filter(title="ministry_leaders").order_by('first_name'):
        #     filtered_leaders.append(leader)

    elif request.POST['title']=="Oikos Leaders (2018-2019)":
        return redirect('/holywave/about/leadership/oikos_leaders')
        # for leader in Leader.objects.filter(title="oikos_leaders").order_by('first_name'):
        #     filtered_leaders.append(leader)

    else:
        return redirect('/holywave/about/leadership')

def leadership_pastors(request):
    filtered_leaders=[]

    for leader in Leader.objects.filter(title__icontains="pastors").order_by('hierarchy', 'first_name'):
        if leader.active:
            filtered_leaders.append(leader)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(filtered_leaders, 12)
    #
    # try:
    #     leaders_list = paginator.page(page)
    # except PageNotAnInteger:
    #     leaders_list = paginator.page(1)
    # except EmptyPage:
    #     leaders_list = paginator.page(paginator.num_pages)


    data={
    "filter_type":"Pastors",
    "leaders_list":filtered_leaders,
    }

    return render(request, 'holywave/about/leadership_filter.html', data)


def leadership_elders(request):
    filtered_leaders=[]

    for leader in Leader.objects.filter(title__icontains="elders").order_by('hierarchy', 'first_name'):
        if leader.active:
            filtered_leaders.append(leader)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(filtered_leaders, 12)
    #
    # try:
    #     leaders_list = paginator.page(page)
    # except PageNotAnInteger:
    #     leaders_list = paginator.page(1)
    # except EmptyPage:
    #     leaders_list = paginator.page(paginator.num_pages)


    data={
    "filter_type":"Elders",
    "leaders_list":filtered_leaders,
    }

    return render(request, 'holywave/about/leadership_filter.html', data)


def leadership_deacons(request):
    filtered_leaders=[]

    for leader in Leader.objects.filter(title__icontains="deacons").order_by('hierarchy', 'first_name'):
        if leader.active:
            filtered_leaders.append(leader)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(filtered_leaders, 12)
    #
    # try:
    #     leaders_list = paginator.page(page)
    # except PageNotAnInteger:
    #     leaders_list = paginator.page(1)
    # except EmptyPage:
    #     leaders_list = paginator.page(paginator.num_pages)


    data={
    "filter_type":"Deacons",
    "leaders_list":filtered_leaders,
    }

    return render(request, 'holywave/about/leadership_filter.html', data)


def leadership_ministry_leaders(request):
    filtered_leaders=[]

    for leader in Leader.objects.filter(title__icontains="ministry_leaders").order_by('hierarchy', 'first_name'):
        if leader.active:
            filtered_leaders.append(leader)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(filtered_leaders, 12)
    #
    # try:
    #     leaders_list = paginator.page(page)
    # except PageNotAnInteger:
    #     leaders_list = paginator.page(1)
    # except EmptyPage:
    #     leaders_list = paginator.page(paginator.num_pages)


    data={
    "filter_type":"Ministry Leaders",
    "leaders_list":filtered_leaders,
    }

    return render(request, 'holywave/about/leadership_filter.html', data)


def leadership_oikos_leaders(request):
    filtered_leaders=[]

    for leader in Leader.objects.filter(title__icontains="oikos_leaders").order_by('hierarchy', 'first_name'):
        if leader.active:
            filtered_leaders.append(leader)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(filtered_leaders, 12)
    #
    # try:
    #     leaders_list = paginator.page(page)
    # except PageNotAnInteger:
    #     leaders_list = paginator.page(1)
    # except EmptyPage:
    #     leaders_list = paginator.page(paginator.num_pages)


    data={
    "filter_type":"Oikos Leaders (2018-2019)",
    "leaders_list":filtered_leaders,
    }

    return render(request, 'holywave/about/leadership_filter.html', data)

def visit_us(request):
    return render(request, 'holywave/about/visit_us.html')




def connect(request):
    return render(request, 'holywave/connect/connect.html')

def im_new(request):
    return render(request, 'holywave/connect/im_new.html')

def oikos(request):
    return render(request, 'holywave/connect/oikos.html')

def membership(request):
    return render(request, 'holywave/connect/membership.html')

def baptism(request):
    return render(request, 'holywave/connect/baptism.html')

def get_involved(request):
    data={
    'ministry_category_list':MinistryCategory.objects.all().order_by('id'),
    }

    return render(request, 'holywave/connect/get_involved.html', data)


def discipleship_training(request):
    return render(request, 'holywave/equip/discipleship_training.html')

def foundations(request):
    return render(request, 'holywave/equip/foundations.html')



def resources(request):
    return render(request, 'holywave/resources/resources.html')

def sermons(request):
    all_sermons = Sermon.objects.all().order_by("-date")


    page = request.GET.get('page', 1)
    paginator = Paginator(all_sermons, 6)

    try:
        sermons_list = paginator.page(page)
    except PageNotAnInteger:
        sermons_list = paginator.page(1)
    except EmptyPage:
        sermons_list = paginator.page(paginator.num_pages)


    data = {
    'all_sermons':Sermon.objects.all().order_by("-date"),
    'sermons_list':sermons_list,
    }

    return render(request, 'holywave/resources/sermons.html', data)

def sermons_search(request):
    if request.POST.get('search_box', None) == None:
        search_query = request.session['sermon_search']

    else:
        search_query = request.POST.get('search_box', None)
        request.session['sermon_search'] = search_query
        request.session.set_expiry(0)

    search_list = []
    for sermon in Sermon.objects.filter(title__icontains=search_query):
        search_list.append(sermon)
    for sermon in Sermon.objects.filter(speaker__icontains=search_query):
        search_list.append(sermon)
    for sermon in Sermon.objects.filter(date__icontains=search_query):
        search_list.append(sermon)

    search_list = [item for item, count in collections.Counter(search_list).items() if count > 0]

    search_list.sort(key=lambda r: r.date, reverse=True)


    page = request.GET.get('page', 1)
    paginator = Paginator(search_list, 6)

    try:
        sermons_list = paginator.page(page)
    except PageNotAnInteger:
        sermons_list = paginator.page(1)
    except EmptyPage:
        sermons_list = paginator.page(paginator.num_pages)


    data = {
    'all_sermons':Sermon.objects.all().order_by("-date"),
    'sermons_list':sermons_list,
    'search_result':search_query,
    }

    if len(search_list)==len(Sermon.objects.all()):
        return redirect('/holywave/resources/sermons')
    else:
        return render(request, 'holywave/resources/sermons_search.html', data)

def sermons_watch(request, sermon_date, sermon_service):
    all_sermons = Sermon.objects.all().order_by("-date")

    page = request.GET.get('page', 1)
    paginator = Paginator(all_sermons, 6)

    try:
        sermons_list = paginator.page(page)
    except PageNotAnInteger:
        sermons_list = paginator.page(1)
    except EmptyPage:
        sermons_list = paginator.page(paginator.num_pages)


    sermon_date = str(sermon_date)
    sermon_date = sermon_date[:4]+"-"+sermon_date[4:]
    sermon_date = sermon_date[:7]+"-"+sermon_date[7:]
    data={
    "this_sermon":Sermon.objects.get(date=sermon_date, service=sermon_service),
    'sermons_list':sermons_list,
    }
    return render(request, 'holywave/resources/sermons_watch.html', data)

def recommended_readings(request):
    all_readings_list=[]
    christian_living_readings_list=[]
    leadership_readings_list=[]
    missions_readings_list=[]
    prayer_readings_list=[]
    theology_readings_list=[]
    wholeness_inner_healing_readings_list=[]

    for reading in Reading.objects.all().order_by("title"):
        all_readings_list.append(reading)

        if reading.category=="christian_living":
            christian_living_readings_list.append(reading)
        if reading.category=="leadership":
            leadership_readings_list.append(reading)
        if reading.category=="missions":
            missions_readings_list.append(reading)
        if reading.category=="prayer":
            prayer_readings_list.append(reading)
        if reading.category=="theology":
            theology_readings_list.append(reading)
        if reading.category=="wholeness_inner_healing":
            wholeness_inner_healing_readings_list.append(reading)


    data={
    'all_readings_list':all_readings_list,
    'christian_living_readings_list':christian_living_readings_list,
    'leadership_readings_list':leadership_readings_list,
    'missions_readings_list':missions_readings_list,
    'prayer_readings_list':prayer_readings_list,
    'theology_readings_list':theology_readings_list,
    'wholeness_inner_healing_readings_list':wholeness_inner_healing_readings_list,
    }

    return render(request, 'holywave/resources/recommended_readings.html', data)


def give(request):
    return render(request, 'holywave/give/give.html')

def give_faq(request):
    return render(request, 'holywave/give/give_faq.html')
