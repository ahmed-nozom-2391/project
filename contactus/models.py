from django.db import models
from django.utils import timezone





class ContactUs(models.Model):
    name       = models.CharField(max_length=30, blank=False, null=False)
    email      = models.EmailField(blank=False, null=False, verbose_name='email address')
    message    = models.TextField( blank=False, null=False )

    created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')
    
    def __str__(self):
        return self.email
    