from django.contrib import admin

from .models import BlogPost
#Modal admin
class BlogPostAdmin(admin.ModelAdmin):
    exclude = ('body',)
    list_display = ('title', 'author')
    list_filter = ('date_published',)
admin.site.register(BlogPost,BlogPostAdmin)


#admin customisation
admin.site.site_header = "DRF Admin Panel"
admin.site.site_title = "Blog post Admin For DRF"
