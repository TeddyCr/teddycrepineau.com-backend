from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from project.api.models import Posts, Profile
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User

def change_is_published_status(modeladmin, request, queryset):
    for post in queryset:
        if post.is_published:
            post.is_published = False
            post.save()
        else:
            post.is_published = True
            post.save()

change_is_published_status.short_description = 'Update post status'

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('title', 'author_id', 'tags','is_published',
                    'creation_date','last_modified')
    list_filter = ('author_id__username','creation_date', 'last_modified')
    list_per_page = 20
    search_fields = ['title']
    actions = [change_is_published_status]
    summernote_fields = ('content',)
    prepopulated_fields = {"slug": ("title",)}

class ProfileAdmin(admin.ModelAdmin):
    pass

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inline = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Posts, PostAdmin)
