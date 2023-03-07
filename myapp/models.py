from django.db import models

# Create your models here.
# name =  models.Model.models.CharField(_(""), max_length=50)
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=1000)


    def __str__(self):
        return 'I got Your Message {self.name}'