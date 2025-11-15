from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15, unique=True)
    nama = models.CharField(max_length=100)
    programstudi = models.CharField(max_length=50)
def __str__(self):
    return self.nim
