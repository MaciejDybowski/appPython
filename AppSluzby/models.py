from django.db import models

# Create your models here.
class Person(models.Model):
    idPerson = models.AutoField(primary_key=True)
    degree = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    numberOfDuty = models.FloatField(default=0)
    numberOfCeremony = models.FloatField(default=0)

class Duty(models.Model):
    DUTY_TYPES = (
        ('Kmp', 'Kompania'),
        ('Sto', 'Stołówka'),
        ('Str', 'Strzelnica'),
        ('Pst', 'PST'),
        ('Bat', 'Batalionowa'),
    )

    idDuty = models.AutoField(primary_key=True)
    typeOfDuty = models.CharField(max_length=3, choices=DUTY_TYPES)
    date = models.DateField()


class Ceremony(models.Model):
    idCeremony = models.AutoField(primary_key=True)
    nameOfCeremony = models.CharField(max_length=50)
    duration = models.FloatField(max_length=4)
    date = models.DateField()

class PersonOnDuty(models.Model):
    idRegistration = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    idDuty = models.ForeignKey(Duty, on_delete=models.CASCADE)

class PersonOnCeremony(models.Model):
    idRegistration = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    idCeremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)


class Soldier(models.Model):
    idSoldier = models.AutoField(primary_key = True)
    degree = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
