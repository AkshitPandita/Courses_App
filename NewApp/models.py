from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    image= models.ImageField(upload_to='course_images/', blank=True, null=True)
    video_id = models.CharField(max_length=11, blank=True, null=True)
    credits = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"
