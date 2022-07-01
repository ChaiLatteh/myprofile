# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Leader(models.Model):
    title=models.CharField(max_length=255)
    sort_title=models.CharField(max_length=255)
    hierarchy=models.CharField(max_length=255, default="1")
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    image=models.ImageField(upload_to="leader_picture", null=True, blank=False)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class UpcomingEvent(models.Model):
    title=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField(null=True, blank=True)
    end_time=models.TimeField(null=True, blank=True)
    location=models.CharField(max_length=255)
    description=tinymce_models.HTMLField()
    # thumbnail_image=models.ImageField(upload_to="upcomingevent_thumbnail", null=True, blank=False)
    image=models.ImageField(upload_to="upcomingevent_picture", null=True, blank=False)

    contact_person=models.CharField(max_length=255)
    contact_email=models.CharField(max_length=255)
    button=models.CharField(max_length=255, null=True, blank=True)
    button_link=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UpcomingClass(models.Model):
    title=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField(null=True, blank=True)
    end_time=models.TimeField(null=True, blank=True)
    location=models.CharField(max_length=255)
    description=tinymce_models.HTMLField()
    # thumbnail_image=models.ImageField(upload_to="upcomingclass_thumbnail", null=True, blank=False)
    image=models.ImageField(upload_to="upcomingclass_picture", null=True, blank=False)

    contact_person=models.CharField(max_length=255)
    contact_email=models.CharField(max_length=255)
    button=models.CharField(max_length=255, null=True, blank=True)
    button_link=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UpcomingEventDraft(models.Model):
    title=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField(null=True, blank=True)
    end_time=models.TimeField(null=True, blank=True)
    location=models.CharField(max_length=255)
    description=tinymce_models.HTMLField()
    # thumbnail_image=models.ImageField(upload_to="upcomingevent_thumbnail", null=True, blank=False)
    image=models.ImageField(upload_to="upcomingevent_picture", null=True, blank=False)

    contact_person=models.CharField(max_length=255)
    contact_email=models.CharField(max_length=255)
    button=models.CharField(max_length=255, null=True, blank=True)
    button_link=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UpcomingClassDraft(models.Model):
    title=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField(null=True, blank=True)
    end_time=models.TimeField(null=True, blank=True)
    location=models.CharField(max_length=255)
    description=tinymce_models.HTMLField()
    # thumbnail_image=models.ImageField(upload_to="upcomingclass_thumbnail", null=True, blank=False)
    image=models.ImageField(upload_to="upcomingclass_picture", null=True, blank=False)

    contact_person=models.CharField(max_length=255)
    contact_email=models.CharField(max_length=255)
    button=models.CharField(max_length=255, null=True, blank=True)
    button_link=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Sermon(models.Model):
    title=models.CharField(max_length=255)
    speaker=models.CharField(max_length=255)
    scripture_passage=models.CharField(max_length=255)
    date=models.DateField()
    video_url=models.CharField(max_length=255)
    service=models.CharField(max_length=255)
    thumbnail_image=models.ImageField(upload_to="sermon_thumbnail", null=True, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.speaker

class MinistryCategory(models.Model):
    ministry_category=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ministry_category

class Ministry(models.Model):
    ministry_category=models.ForeignKey(MinistryCategory, related_name="ministries", on_delete=models.SET_NULL, null=True)
    ministry_name=models.CharField(max_length=255)
    description=tinymce_models.HTMLField()
    contact_person=models.CharField(max_length=255)
    contact_email=models.CharField(max_length=255)

    contact_extra=models.CharField(max_length=255, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ministry_name

class Reading(models.Model):
    reading_cover=models.ImageField(upload_to="reading_cover", blank=False)
    category=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    summary=tinymce_models.HTMLField()
    pdf_link=models.CharField(max_length=255, blank=True)
    pdf_button=models.CharField(max_length=255, blank=True)
    purchase_link=models.CharField(max_length=255, blank=True)
    purchase_button=models.CharField(max_length=255, blank=True)
    display=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Button(models.Model):
    name=models.CharField(max_length=255)
    button=models.CharField(max_length=255)
    application_link=models.CharField(max_length=255)
    active=models.BooleanField()
    closed_application_notice=models.CharField(max_length=255, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
