from django.db import models

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_cargo

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mes(models.Model):
    nombre_mes = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_mes

class Calculo(models.Model):
    empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, null=True, blank=True, on_delete=models.CASCADE)
    desAFP = models.DecimalField(decimal_places=2, max_digits=10)
    desRENTA = models.DecimalField(decimal_places=2, max_digits=10)
    desISSS = models.DecimalField(decimal_places=2, max_digits=10)
    fecha_pago = models.DateTimeField(default='2023-12-31 12:00')

    def __str__(self):
        return f"Calculo para {self.empleado} en {self.mes}"

class Bitacora(models.Model):
    accion = models.CharField(max_length=30)
    empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.accion} - {self.empleado}"
