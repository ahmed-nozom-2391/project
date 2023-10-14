from django.db import models
from user.models import MyUser
from django.utils import timezone





class AccountMessage(models.Model):
    created_by    = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='created by')
    created_at    = models.DateTimeField(default=timezone.now, verbose_name='created at')
    message       = models.TextField( blank=False, null=False ) 
    
    def __str__(self):
        return self.id
    