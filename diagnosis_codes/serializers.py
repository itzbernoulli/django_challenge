from rest_framework import serializers
from .models import DiagnosisCode

class DiagnosisCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiagnosisCode
		fields = ('id',
				'category_code',
				'diagnosis_code',
				'full_code',
				'abbreviated_description',
				'full_description',
				'category_title',
				'created_at',
				'updated_at')
