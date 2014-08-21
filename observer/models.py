from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
	detail = models.CharField(max_length=50)

class Surat(models.Model):
	perihal = models.CharField(max_length=200)
	asal = models.CharField(max_length=200)
	keterangan = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class LogSurat(models.Model):
	user = models.ForeignKey(User)
	surat = models.ForeignKey(Surat)
	log = models.ForeignKey(Status)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
