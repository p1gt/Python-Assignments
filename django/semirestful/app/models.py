from django.db import models

class showManager(models.Manager):
    def basic_validator(self,postdata):
        errors = {}
        if len(postdata['title']) < 2:
            errors['title'] = 'Title must be at least 2 characters'
        if len(postdata['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'
        if len(postdata['desc']) < 10:
            errors['desc'] = 'Description must be at least 10 characters'
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = showManager()