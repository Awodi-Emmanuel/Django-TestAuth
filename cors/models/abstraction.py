from datetime import datetime
from random import choices
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import BooleanField

User = get_user_model()

class TempCode(models.MOdel):
  TYPES = [
    ('signin', 'signin'),
    ('signup', 'signup'),
    ('reset', 'reset'),
    ('invite', 'invite'),
  ]
  code: models.CharField(max_length=255)
  type = models.CharField = models.CharField(max_length=10, choices=TYPES)
  created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
  expires: models.DateTimeField = models.DateTimeField()
  is_used: models.BooleanField = BooleanField(default=True) 
  user: models.ForeignKey = models.ForeignKey(User, models.CASCADE)
  
  class Meta:
    abstract = True
    
class UserSettings(models.Model):
  lang: models.CharField = models.CharField(max_length=3, default='en')
  push_channel: models.CharField = models.CharField(max_length=255, null=True,blank=True)
  
  class Meta:
    abstract = True      
class Profile(models.Models):
  country:models.CharField = models.CharField(max_length=50)
  address: models.CharField = models.CharField(max_length=255)
  city: models.CharField = models.CharField(max_length=255)
  state: models.CharField  = models.CharField(max_length=255, null=True, blank=True)
  zip_code: models.CharField = models.CharField(max_length=10)
  phone_number: models.CharField = models.CharField(max_length=20)
  contact_name: models.CharField = models.CharField(max_length=255)
  contact_country: models.CharField = models.CharField(max_length=50)
  contact_address: models.CharField = models.CharField(max_length=255)
  contact_city: models.CharField = models.CharField(max_length=255)
  contact_state: models.CharField = models.CharField(max_length=255, null=True, blank=True)
  contact_zipcode: models.CharField = models.CharField(max_length=10)
  contact_phone_number: models.CharField = models.CharField(max_length=20)
  user: models.OneToOneField = models.OneToOneField(User, models.CASCADE)  
  
  class Meta:
    abstract = True
  
  
        