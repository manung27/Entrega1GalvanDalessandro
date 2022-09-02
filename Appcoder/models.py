from django.db import models

class Renault(models.Model):
    modelo=models.CharField(max_length=50)
    velocidad=models.IntegerField()
    caballos_fuerza=models.IntegerField()

#models.IntegerField() numeros
    def __str__(self):
        return self.modelo+" "+str(self.velocidad)+str(self.caballos_fuerza)
#recordar agregar a las otras class
class Ford(models.Model):
    modelo=models.CharField(max_length=50)
    velocidad=models.IntegerField()
    caballos_fuerza=models.IntegerField()

class Volkswagen(models.Model):
    modelo=models.CharField(max_length=50)
    velocidad=models.IntegerField()
    caballos_fuerza=models.IntegerField()




    

