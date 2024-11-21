from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
