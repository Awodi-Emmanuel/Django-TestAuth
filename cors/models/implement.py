from django.utils import timezone
from abstraction import Profile as AbstractProfile
from .abstraction import UserSettings as AbstractUserSettings
from .abstraction import TempCode as AbstractTempCode

class TempCode(AbstractTempCode):
  def save(self, *args, **kwargs):
    from datetime import timedelta
    
    self.expires = timezone.now() + timedelta(minutes=10)
    super().save(*args, **kwargs)
    
  @classmethod
  
  def get_string_code() 