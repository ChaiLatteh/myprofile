from django.db import models

from tinymce import models as tinymce_models


# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=255, blank=True)
    menu_categories=[
    ('', 'Select'),
    ('smoothie', 'Smoothie'),
    ('special_smoothie', 'Special Smoothie'),
    ('special_drink', 'Special Drink'),
    ('slush', 'Slush'),
    ('milk_tea', 'Milk Tea'),
    ('jasmine_tea', 'Jasmine Green Tea'),
    ('frappe', 'Frappe'),
    ('milkshake', 'Milkshake'),
    ('waffle', 'Waffle'),
    ('milk_snow', 'Milk Snow'),
    ('acai_pitaya', 'Acai & Pitaya'),
    ('cafe', 'Cafe'),
    ('hot_tea', 'Hot Tea'),
    ('ice_cream', 'Ice Cream'),
    ('taiyaki', 'Taiyaki'),
    ]
    category=models.CharField(max_length=255, choices=menu_categories)
    description=tinymce_models.HTMLField(blank=True)
    image=models.ImageField(upload_to="menu_item_image", null=True, blank=True)

    def __str__(self):
        return self.category + "-" + self.name
