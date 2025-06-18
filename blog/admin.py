from django.contrib import admin
from .models import Post , Section


admin.site.register(Post)
class SectionAdmin(admin.ModelAdmin):
    ordering = ('post__created_date','order')
admin.site.register(Section, SectionAdmin)