from django.db import models

class Dogs(models.Model):
    byname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    breed = models.CharField(max_length=20)
    
class Curators(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)

class Costs(models.Model):
    dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)
    date = models.DateField()
    treatment = models.CharField(max_length=20)
    veterinarian = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=7, decimal_places=2)


#class Veterinarians:
#    pass

#class Blacklist: - linked to Curators
#    pass

#class Treatment_etc:
#    pass
