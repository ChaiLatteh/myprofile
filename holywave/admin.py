from django.contrib import admin
from .models import Leader, UpcomingEvent, UpcomingClass, UpcomingEventDraft, UpcomingClassDraft, Sermon, MinistryCategory, Ministry, Reading, Button

# Register your models here.
admin.site.register(Leader)
admin.site.register(UpcomingEvent)
admin.site.register(UpcomingClass)
admin.site.register(UpcomingEventDraft)
admin.site.register(UpcomingClassDraft)
admin.site.register(Sermon)
admin.site.register(MinistryCategory)
admin.site.register(Ministry)
admin.site.register(Reading)
admin.site.register(Button)
