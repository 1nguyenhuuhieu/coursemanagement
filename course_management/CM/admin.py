from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'course_price','status')
    list_filter = ('course', 'status')
    change_list_template: 'admin/change_list.html'

    def get_total(self):  
        pursched = UserCourse.objects.filter(status='purchased')
        total = sum(i.course.price for i in pursched)
        return total

    def changelist_view(self, request, extra_context = None):
        context = {
            'total': self.get_total(),

        }

        return super(UserCourseAdmin, self).changelist_view(
            request, extra_context=context
        )

    @admin.display(empty_value='???')
    def course_price(self, obj):
        return obj.course.price
    def total(self, obj):
        
        pursched = UserCourse.objects.filter(status='purchased')
        total = sum(i.course.price for i in pursched)
        return total


@admin.register(CourseReaction)
class CourseReactionAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    pass