from django.db import models
import project_name.settings as settings
import bcrypt

class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=60)
  last_4_digits = models.CharField(max_length=4, blank=True, null=True)
  stripe_id = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email

  def set_password(self, clear_password):
    salt = bcrypt.gensalt(settings.BCRYPT_ROUNDS)
    self.password = bcrypt.hashpw(clear_password, salt)
  
  def check_password(self, clear_password):
    return bcrypt.hashpw(clear_password, self.password) == self.password