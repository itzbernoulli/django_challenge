from django.test import TestCase
from ..models import DiagnosisCode

# Create your tests here.
class DiagnosisCodeTest(TestCase):
	""" Test module for DiagnosisCode model """
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

	def test_diagnosis_code(self):
		codeAO = DiagnosisCode.objects.get(category_code='A0')
		codeB730 = DiagnosisCode.objects.get(category_code='B730')
		self.assertEqual(codeAO.get_diagnosis(),"1234 is in category A0 with full code A01234")
		self.assertEqual(codeB730.get_diagnosis(),"9 is in category B730 with full code B7309")