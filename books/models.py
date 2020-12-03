from django.db import models


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    label = models.CharField(max_length=50)
    main_pic = models.ImageField(null=True,blank=True,upload_to='images')
    second_pic = models.ImageField(null=True,blank=True,upload_to='images')
    main_detail = models.TextField()
    second_detail = models.TextField()

    def __str__(self):
        return self.title