from django.db import models
from user.models import MyUser
from django.utils import timezone





class Ticket(models.Model):
    created_by    = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='created by')
    created_at    = models.DateTimeField(default=timezone.now, verbose_name='created at')

    suitable_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='suitable time for contact')
    company_name  = models.CharField( max_length=50, blank=False, null=False, verbose_name='company name' )
    work_field    = models.CharField( max_length=50, blank=False, null=False, verbose_name='work field')
    problem_type  = models.CharField( max_length=50, blank=False, null=False, verbose_name='problem type' )
    message       = models.TextField( blank=False, null=False ) 
    
    def __str__(self):
        return self.problem_type
    