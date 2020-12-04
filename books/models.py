from django.db import models
from django.utils.translation import gettext_lazy as _

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(_('Title'),max_length=20,default='', blank=False, null=False)
    label = models.CharField(_('Label'),max_length=100, blank=True,null=True)
    main_pic = models.ImageField(_('Main_pic'),null=True,blank=True,upload_to='images')
    second_pic = models.ImageField(_('Second_pic'),null=True,blank=True,upload_to='images')
    main_detail = models.TextField(_('Main_detail'), null=True, blank=True)
    second_detail = models.TextField(_('Second_detail'), null=True, blank=True)

    def __str__(self):
        return self.title