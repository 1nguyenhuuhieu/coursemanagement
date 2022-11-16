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
    list_display = ('user', 'course', 'course_price','status')
    list_filter = ('course', 'status')

    @admin.display(empty_value='???')
    def course_price(self, obj):
        return obj.course.price

@admin.register(CourseReaction)
class CourseReactionAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    pass