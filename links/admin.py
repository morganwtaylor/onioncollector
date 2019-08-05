from django.contrib import admin
from . import models

class LinkInline(admin.TabularInline):
    model=models.Link
    classes=['collapse']

class ReviewInline(admin.TabularInline):
    model = models.Review
    classes=['collapse']



class CategoryAdmin(admin.ModelAdmin):
    inlines=[LinkInline,]
    fields = ['title']
    def number_of_links(self, Category):
        return '{} links'.format(Category.links.count())
    list_display= ['title', 'number_of_links']

class LinkAdmin(admin.ModelAdmin):
    inlines=[ReviewInline]
    fields = ['user', 'link', 'category', 'nsfw', 'votes', 'title', 'description', 'featured', 'approved']
    search_fields = ['title', 'description', 'link']
    list_filter=['created_at']

    list_display =['title', 'link', 'created_at', 'votes', 'category']

    list_editable=['category']

class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'link', 'title']


admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Review, ReviewAdmin)
