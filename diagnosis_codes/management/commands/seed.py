from django.core.management.base import BaseCommand
import random
import logging
from ...models import DiagnosisCode
import csv
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))
import sys

class Command(BaseCommand):
	help = "seed database for development"
	logger = logging.getLogger(__name__)

	def add_arguments(self, parser):
		parser.add_argument('--mode', type=str, help="Mode")

	def handle(self, *args, **options):
		self.stdout.write('seeding data...')
		run_seed(self, options['mode'])
		self.stdout.write('Done.')

def clear_data():
    """Deletes all the table data"""
    DiagnosisCode.objects.all().delete()

def create_diagnosis_code_from_csv():
	with open(os.path.join(BASE,'codes.csv')) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		count = 0
		for row in readCSV:
			diagnosis = DiagnosisCode(
			category_code = row[0],
			diagnosis_code = row[1],
			full_code = row[2],
			abbreviated_description = row[3],
			full_description = row[4],
			category_title = row[5])
			diagnosis.save()
			count = count + 1
			msg = "%i " % (count)
			sys.stdout.write(msg + chr(8) * len(msg))
			sys.stdout.flush()


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()

    #create new database records
    create_diagnosis_code_from_csv()
