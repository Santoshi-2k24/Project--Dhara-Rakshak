from django.db import models

class LandRecord(models.Model):
 full_name = models.CharField(max_length=100)
 mandal = models.CharField(max_length=100)
 district = models.CharField(max_length=100)
 state = models.CharField(max_length=100)
 aadhar_number = models.CharField(max_length=12, unique=True)
 document_number = models.CharField(max_length=50)
 survey_number = models.CharField(max_length=50)
 photo = models.ImageField(upload_to='land_photos/')
 registered_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.full_name} - {self.survey_number}"
