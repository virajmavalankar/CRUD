from django.db import models

class UserModel(models.Model):
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	phonenumber = models.CharField(max_length = 100)
	class Meta:
		db_table = "employee"
