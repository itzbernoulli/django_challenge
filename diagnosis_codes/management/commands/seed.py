from django.core.management.base import BaseCommand
import random
import logging
from ...models import DiagnosisCode
import csv
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

class Command(BaseCommand):
	help = "seed database for development"
	logger = logging.getLogger(__name__)

	def add_arguments(self, parser):
		parser.add_argument('--mode', type=str, help="Mode")

	def handle(self, *args, **options):
		self.stdout.write('seeding data...')
		run_seed(self, options['mode'])
		self.stdout.write('done.')

def clear_data():
    """Deletes all the table data"""
    # logger.info("Delete Address instances")
    DiagnosisCode.objects.all().delete()


def create_diagnosis_code():
    """Creates DiagnosisCode object combining different elements from the list"""
    # logger.info("Creating address")
    street_flats = ["#21B", "#10A", "#55I", "#40G", "#A3"]
    street_localities = ["Bakers Street", "Rajori Gardens", "Park Street", "MG Road", "Indiranagar"]
    pincodes = ["101234", "101232", "101231", "101236", "101239"]

    diagnosis = DiagnosisCode(
			category_code = random.choice(street_flats),
			diagnosis_code = random.choice(street_flats),
			full_code = random.choice(pincodes),
			abbreviated_description = random.choice(street_localities),
			full_description = random.choice(street_localities),
			category_title = random.choice(street_localities))

    diagnosis.save()
    # logger.info("{} diagnosis created.".format(diagnosis))
    return diagnosis

def create_diagnosis_code_from_csv():
	with open(os.path.join(BASE,'codes.csv')) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			# print(row)
			diagnosis = DiagnosisCode(
			category_code = row[0],
			diagnosis_code = row[1],
			full_code = row[2],
			abbreviated_description = row[3],
			full_description = row[4],
			category_title = row[5])
			diagnosis.save()
			print("{} diagnosis created.".format(diagnosis.category_code))


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    # if mode == MODE_CLEAR:
    #     return

    create_diagnosis_code_from_csv()
	# with open('codes.csv') as csvfile:
	# 	readCSV = csv.reader(csvfile, delimiter=',')
	# 	for row in readCSV:
	# 		print(row)
	# 		print(row[0])

    # Creating 15 addresses
    # for i in range(15):
    #     create_diagnosis_code()