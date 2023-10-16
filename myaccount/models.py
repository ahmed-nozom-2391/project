from django.db import models
from user.models import MyUser
from django.utils import timezone
from service.models import Service




class AccountMessage(models.Model):
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='created by')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')
    message    = models.TextField( blank=False, null=False ) 
    
    def __str__(self):
        return str(self.id)
    

class MyService(models.Model):
    user       = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    service    = models.ForeignKey(Service, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "My cart"
        verbose_name_plural = "My cart"
    