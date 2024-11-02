from django.contrib import admin

from contacs.models import Contact, Person

# Register your models here.
admin.site.register(Contact)
admin.site.register(Person)