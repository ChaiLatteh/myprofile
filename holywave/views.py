from django.shortcuts import render, redirect

from .models import Leader, UpcomingEvent, UpcomingClass, UpcomingEventDraft, UpcomingClassDraft, Sermon, MinistryCategory, Ministry, Reading, Button

# Create your views here.
def home(request):
    return render(request, 'holywave/home.html')

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
    return render(request, 'holywave/resources/sermons.html')

def sermons_search(request):
    return render(request, 'holywave/resources/sermons_search.html')

def sermons_watch(request):
    return render(request, 'holywave/resources/sermons_watch.html')

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
