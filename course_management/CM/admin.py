from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseReaction)
class CourseReactionAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    pass