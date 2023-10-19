from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import os
from project import settings
from django.core.files.storage import FileSystemStorage
from random import choice
from string import ascii_lowercase, digits
import datetime



def validate_name(name):
    if not(name) or name.isspace():
        raise ValidationError('empty name is not valid name') 
    for char in name:
        if not char.isalpha() and char != ' ':
            raise ValidationError('special characters not allowed') 
    if name.startswith(' '):
            raise ValidationError('name can not start with space')
    if name.endswith(' '):
            raise ValidationError('name can not end with space')
    if name.count(' ') > 1 :
         raise ValidationError('name can not contain more than one space')
    




def generate_name(length=4, chars = ascii_lowercase+digits):
    '''generate name from two sections
        1. random name of 4 letters from chars list
        2. current date and time
    '''
    random_name = ''.join([choice(chars) for i in range(length)])
    dt = datetime.datetime.now()
    dt_str = dt.strftime("%Y%m%d%H%M%S")
    return "%s-%s"%(random_name, dt_str)



def image_upload(instance, filename):
    imgname, *exten = filename.split(".")
    new_name = generate_name() 
    return "user/%s.%s"%(new_name, exten[-1])



class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length = None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name




class MyUser(AbstractUser):
    email         = models.EmailField(unique=False, blank=False, null=False, verbose_name='email address')
    phone_regex   = RegexValidator(regex="[0][1][0125][0-9][ ]?\d{3}[ ]?\d{4}", message="Phone number must be entered in the format: '01xx xxx xxxx'. Up to 11 digits allowed.")
    phone         = models.CharField(unique=True, validators=[phone_regex], max_length=11, blank=False, null=False, verbose_name='phone') # validators should be a list
    first_name    = models.CharField(validators=[validate_name], max_length=30, blank=False, null=False, verbose_name='first name')
    last_name     = models.CharField(validators=[validate_name], max_length=30, blank=True, null=True, verbose_name='last name')
    
    avatar        = models.ImageField(upload_to=image_upload, default = 'user/avatar.png', storage = OverwriteStorage() )

    company_name    = models.CharField(validators=[validate_name], max_length=50, blank=False, null=False, verbose_name='company name')
    work_field      = models.CharField(validators=[validate_name], max_length=50, blank=False, null=False, verbose_name='work field')


    REQUIRED_FIELDS = ['phone', 'email', 'first_name', 'company_name', 'work_field']


    def __str__(self):
        return self.phone


    
    @property
    def get_name(self):
        name = self.first_name
        if self.last_name:
            name += ' ' + self.last_name
        return name
        

        