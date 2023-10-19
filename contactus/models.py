from django.db import models
from django.utils import timezone





class ContactUs(models.Model):
    name       = models.CharField(max_length=30, blank=False, null=False)
    email      = models.EmailField(blank=False, null=False, verbose_name='email address')
    message    = models.TextField( blank=False, null=False )

    created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
    

class ContactInfo(models.Model):
    call_us      = models.CharField(max_length=50, blank=True, null=True)
    email        = models.EmailField()
    offices      = models.CharField(max_length=50, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True, verbose_name='facebook url')
    twitter_url  = models.URLField(blank=True, null=True, verbose_name='twitter url')
    whatsapp_url = models.URLField(blank=True, null=True, verbose_name='whatsapp url')
    linkedin_url = models.URLField(blank=True, null=True, verbose_name='linkedin url')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"