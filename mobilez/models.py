from django.db import models
from snippets.models import MyUser

# Create your models here.

class TodoMobilez(models.Model):
    mobile = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.mobile