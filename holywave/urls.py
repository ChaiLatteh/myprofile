from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    # path('about/who_we_are', views.who_we_are, name="who_we_are"),
    path('about/our_story', views.our_story, name="our_story"),
    path('about/leadership', views.leadership, name="leadership"),
    path('about/leadership_filter', views.leadership_filter, name="leadership_filter"),
    path('about/leadership/pastors', views.leadership_pastors, name="leadership_pastors"),
    path('about/leadership/elders', views.leadership_elders, name="leadership_elders"),
    path('about/leadership/deacons', views.leadership_deacons, name="leadership_deacons"),
    path('about/leadership/ministry_leaders', views.leadership_ministry_leaders, name="leadership_ministry_leaders"),
    path('about/leadership/oikos_leaders', views.leadership_oikos_leaders, name="leadership_oikos_leaders"),
    path('about/visit_us', views.visit_us, name="visit_us"),

    path('connect', views.connect, name="connect"),
    path('connect/im_new', views.im_new, name="im_new"),
    path('connect/oikos', views.oikos, name="oikos"),
    path('connect/membership', views.membership, name="membership"),
    path('connect/baptism', views.baptism, name="baptism"),
    path('connect/get_involved', views.get_involved, name="get_involved"),

    path('equip/dt', views.discipleship_training, name="discipleship_training"),
    path('equip/foundations', views.foundations, name="foundations"),

    path('resources', views.resources, name="resources"),
    path('resources/sermons', views.sermons, name="sermons"),
    path('resources/sermons/search', views.sermons_search, name="sermons_search"),
    # path('resources/sermons/(?P<sermon_date>\w+)-(?P<sermon_service>\w+)', views.sermons_watch, name="sermons_watch"),
    path('resources/recommended_readings', views.recommended_readings, name="recommended_readings"),

    path('give', views.give, name="give"),
    path('give/faq', views.give_faq, name="give_faq"),

]
