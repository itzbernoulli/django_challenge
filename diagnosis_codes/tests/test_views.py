import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import DiagnosisCode
from ..serializers import DiagnosisCodeSerializer

#initialize the APIClient app
client = Client()

class GetAllDiagnosisCodesTest(TestCase):
	""" Test module for GET all diagnosis API """

	def setUp(self):
		DiagnosisCode.objects.create(
			category_code = 'A0',
			diagnosis_code = '1234',
			full_code = 'A01234',
			abbreviated_description = 'Comma-ind anal ret',
			full_description = 'Comma-induced anal retention',
			category_title = 'Malignant neoplasm of anus and anal canal')
		DiagnosisCode.objects.create(
			category_code = 'B730',
			diagnosis_code = '9',
			full_code = 'B7309',
			abbreviated_description = 'Onchocerciasis with other eye involvement',
			full_description = 'Onchocerciasis with other eye involvement',
			category_title = 'Onchocerciasis with eye disease')
		DiagnosisCode.objects.create(
			category_code = 'B72',
			diagnosis_code = '',
			full_code = 'B72',
			abbreviated_description = 'Dracunculiasis',
			full_description = 'Dracunculiasis',
			category_title = 'Dracunculiasis')


	def test_get_all_diagnosis_codes(self):
		#get API Response
		response = client.get(reverse('get_post_diagnosis'))
		#get data from db
		diagnosis = DiagnosisCode.objects.all()
		serializer = DiagnosisCodeSerializer(diagnosis, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleDiagnosisTest(TestCase):
	""" Test module for GET single diagnosis API """

	def setUp(self):
		self.code1 = DiagnosisCode.objects.create(
			category_code = 'A0',
			diagnosis_code = '1234',
			full_code = 'A01234',
			abbreviated_description = 'Comma-ind anal ret',
			full_description = 'Comma-induced anal retention',
			category_title = 'Malignant neoplasm of anus and anal canal')
		self.code2 = DiagnosisCode.objects.create(
			category_code = 'B730',
			diagnosis_code = '9',
			full_code = 'B7309',
			abbreviated_description = 'Onchocerciasis with other eye involvement',
			full_description = 'Onchocerciasis with other eye involvement',
			category_title = 'Onchocerciasis with eye disease')
		self.code3 = DiagnosisCode.objects.create(
			category_code = 'B72',
			diagnosis_code = '',
			full_code = 'B72',
			abbreviated_description = 'Dracunculiasis',
			full_description = 'Dracunculiasis',
			category_title = 'Dracunculiasis')

	def test_get_valid_single_diagnosis_code(self):
		response = client.get(
			reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.code1.pk}))
		diagnosis = DiagnosisCode.objects.get(pk=self.code1.pk)
		serializer = DiagnosisCodeSerializer(diagnosis)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_diagnosis_code(self):
		response = client.get(reverse('get_delete_update_diagnosis_code', kwargs={'pk':30}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewDiagnosisCodeTest(TestCase):
	""" Test module for inserting a new Diagnosis Code """

	def setUp(self):
		self.valid_payload = {
		'category_code' : 'B730',
		'diagnosis_code' : '9',
		'full_code' : 'B7309',
		'abbreviated_description' : 'Onchocerciasis with other eye involvement',
		'full_description' : 'Onchocerciasis with other eye involvement',
		'category_title' : 'Onchocerciasis with eye disease'
		}
		self.invalid_payload = {
		'category_code' : 'B730',
		'diagnosis_code' : '',
		'full_code' : 'B7309',
		'abbreviated_description' : 'Onchocerciasis with other eye involvement',
		'full_description' : 'Onchocerciasis with other eye involvement',
		'category_title' : 'Onchocerciasis with eye disease'
		}

	def test_create_valid_diagnosis_code(self):
		response = client.post(
			reverse('get_post_diagnosis'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_diagnosis(self):
		response = client.post(
			reverse('get_post_diagnosis'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleDiagnosisCodeTest(TestCase):
	""" Test module for updating a single Diagnosis Code """

	def setUp(self):
		self.code1 = DiagnosisCode.objects.create(
			category_code = 'A0',
			diagnosis_code = '1234',
			full_code = 'A01234',
			abbreviated_description = 'Comma-ind anal ret',
			full_description = 'Comma-induced anal retention',
			category_title = 'Malignant neoplasm of anus and anal canal')
		self.code2 = DiagnosisCode.objects.create(
			category_code = 'B730',
			diagnosis_code = '9',
			full_code = 'B7309',
			abbreviated_description = 'Onchocerciasis with other eye involvement',
			full_description = 'Onchocerciasis with other eye involvement',
			category_title = 'Onchocerciasis with eye disease')

		self.valid_payload = {
		'category_code' : 'B730',
		'diagnosis_code' : '9',
		'full_code' : 'B7309',
		'abbreviated_description' : 'Onchocerciasis with other eye involvement',
		'full_description' : 'Onchocerciasis with other eye involvement',
		'category_title' : 'Onchocerciasis with eye disease'
		}
		self.invalid_payload = {
		'category_code' : '',
		'diagnosis_code' : '',
		'full_code' : 'B7309',
		'abbreviated_description' : 'Onchocerciasis with other eye involvement',
		'full_description' : 'Onchocerciasis with other eye involvement',
		'category_title' : 'Onchocerciasis with eye disease'
		}

	def test_valid_update_diagnosis_code(self):
		response = client.put(
			reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.code1.pk}),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_update_diagnosis(self):
		response = client.put(
			reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.code1.pk}),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class DeleteSingleDiagnosisCode(TestCase):
	""" Test module for deleting an existing diagnosis code record """
	def setUp(self):
		self.code1 = DiagnosisCode.objects.create(
			category_code = 'A0',
			diagnosis_code = '1234',
			full_code = 'A01234',
			abbreviated_description = 'Comma-ind anal ret',
			full_description = 'Comma-induced anal retention',
			category_title = 'Malignant neoplasm of anus and anal canal')
		self.code2 = DiagnosisCode.objects.create(
			category_code = 'B730',
			diagnosis_code = '9',
			full_code = 'B7309',
			abbreviated_description = 'Onchocerciasis with other eye involvement',
			full_description = 'Onchocerciasis with other eye involvement',
			category_title = 'Onchocerciasis with eye disease') 

		def test_valid_delete_diagnosis_code(self):
			response = client.delete(
				reverse('get_delete_update_diagnosis_code', kwargs={'pk': self.code1.pk}))
			self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		def test_invalid_delete_diagnosis_code(self):
			response = client.delete(
				reverse('get_delete_update_diagnosis_code', kwargs={'pk': 30}))
			self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




