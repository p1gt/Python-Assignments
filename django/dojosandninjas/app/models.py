from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def get_all_dojos():
    return Dojos.objects.all()    


def get_all_ninja():
    return Ninjas.objects.all() 

def add_ninja(request):
    first_name = request.POST['first_name']
    last_name =  request.POST['last_name']
    dojo_id = request.POST['dojo_id']
    newNinjia = Ninjas.objects.create(first_name=first_name, last_name=last_name, dojo_id=dojo_id)
    return newNinjia

def addDojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    newDojo = Dojos.objects.create(name=name,city=city,state=state)
    return newDojo