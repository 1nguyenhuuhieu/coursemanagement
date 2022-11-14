from secrets import choice
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    descreption = models.CharField(max_length=1000)
    price = models.IntegerField()
    videos = models.ManyToManyField('Video', blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    courses = models.ManyToManyField(Course, blank=True)
    title = models.CharField(max_length=200)
    descreption = models.CharField(max_length=1000)
    url = models.FileField()

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.title

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_added = models.TimeField(auto_now=True)
    STATUS_CHOICES = [
        ('added','Đã thêm vào giỏ hàng'),
        ('waiting', 'Đang chờ thanh toán'),
        ('purchased', 'Đã thanh toán')
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='added')

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user}, {self.course}"

class CourseReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_added = models.TimeField(auto_now=True)
    STATUS_CHOICES = [
    ('like','Thích'),
    ('dislike', 'Không thích')
    ]
    RATE_CHOICES = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    ]
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    rate = models.IntegerField(choices=RATE_CHOICES)

class CourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_added = models.TimeField(auto_now=True)
    comment = models.CharField(max_length=1000)

class VideoReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Video, on_delete=models.CASCADE)
    time_added = models.TimeField(auto_now=True)
    STATUS_CHOICES = [
    ('like','Thích'),
    ('dislike', 'Không thích')
    ]
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    rate = models.IntegerField()

class VideoComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Video, on_delete=models.CASCADE)
    time_added = models.TimeField(auto_now=True)
    comment = models.CharField(max_length=1000)




