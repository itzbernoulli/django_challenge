from django.db import models

# Create your models here.
class DiagnosisCode(models.Model):
	category_code = models.CharField(max_length=10)
	diagnosis_code = models.CharField(max_length=10)
	full_code = models.CharField(max_length=10)
	abbreviated_description = models.CharField(max_length=100)
	full_description = models.CharField(max_length=255)
	category_title = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __repr__(self):
		return self.diagnosis_code + ' is added.'

	def get_diagnosis(self):
		return self.diagnosis_code + ' is in category ' + self.category_code + ' with full code ' + self.full_code