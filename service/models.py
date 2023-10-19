from django.db import models
from user.models import MyUser
from django.core.exceptions import ValidationError
import os
from project import settings
from django.core.files.storage import FileSystemStorage
from random import choice
from string import ascii_lowercase, digits
import datetime
from django.utils import timezone
from django.core.files.images import get_image_dimensions




def validate_name(name):
    if not(name) or name.isspace():
        raise ValidationError('empty name is not valid name')   




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
    return "service/%s.%s"%(new_name, exten[-1])



class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length = None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def validate_dimension(image):
    width, height = get_image_dimensions(image)
    if width != 683 or height !=  1024:
        raise ValidationError(
            [f'Size should be  683*1024.']
            )
    


class ServiceSegment(models.Model):
    title       = models.CharField(max_length=60 ,blank=False, null=False)
    image       = models.ImageField(    
                                         upload_to=image_upload,
                                         validators=[validate_dimension],
                                         default = 'service/service.jpg',
                                         storage = OverwriteStorage() 
                                     )
    figcaption  = models.CharField(max_length=200 ,blank=True, null=True)
    details     = models.TextField(blank=False, null=False) 

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    

    
    def __str__(self):
        return str(self.id)


class Service(models.Model):
    created_by   = models.ForeignKey(MyUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='created by')
    created_at   = models.DateTimeField(default=timezone.now, verbose_name='created at')
    service_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='service name')
    image        = models.ImageField(    
                                         upload_to=image_upload,
                                         validators=[validate_dimension],
                                         default = 'service/service.jpg',
                                         storage = OverwriteStorage() 
                                     )
    details      = models.CharField(max_length=82, blank=False, null=False) 
    slug         = models.SlugField(max_length = 255, null = False, blank = False, unique=True)

    segments     = models.ManyToManyField(ServiceSegment, blank = True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    

    
    def __str__(self):
        return self.service_name
    