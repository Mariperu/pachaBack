from django.db import models

# Create your models here.
class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=13)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    pais = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    
class Avion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class TipoAsiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class Asiento(models.Model):
    id = models.AutoField(primary_key=True)
    columna = models.CharField(max_length=2)
    fila = models.IntegerField()
    tipoAsiento = models.ForeignKey(TipoAsiento, on_delete=models.CASCADE)
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Vuelo(models.Model):
    id = models.AutoField(primary_key=True)
    fechaTakeOff = models.DateTimeField()
    aeropuertoTakeOff = models.CharField(max_length=200)
    fechaLanding = models.DateTimeField()
    aeropuertoLanding = models.CharField(max_length=200)
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    
class BoardingPass(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    tipoAsiento = models.ForeignKey(TipoAsiento, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    

