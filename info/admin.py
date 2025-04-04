from django.contrib import admin
from .models import Competence, Education, Experience, Project, Message, Information


admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Competence)
admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'show_in_slider')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'description')
admin.site.register(Message)



