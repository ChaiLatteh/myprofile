# Generated by Django 4.0.5 on 2022-07-01 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holywave', '0002_button_created_at_button_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingclass',
            name='button',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingclass',
            name='button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingclassdraft',
            name='button',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingclassdraft',
            name='button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingevent',
            name='button',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingevent',
            name='button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingeventdraft',
            name='button',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='upcomingeventdraft',
            name='button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
