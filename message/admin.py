from django.contrib import admin

# Register your models here.

from message.models import Category, ContactMessage

admin.site.register(Category)
admin.site.register(ContactMessage)

