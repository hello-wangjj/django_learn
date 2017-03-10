from django.contrib import admin
from hello.models import *
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'state_province',
        'country',
        'website')
    search_fields = ('name', )
    list_filter = ('city', )
    ordering = ('id', )
    # fields = ('name', 'city')
    # exclude = ('website',)
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'city', 'state_province')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('country', 'website'),
        }),
    )

admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book)