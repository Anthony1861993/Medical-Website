
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from patients.models import Patient

from pyexcel_xlsx import get_data
from decimal import Decimal
data = get_data("Sample_data_assignment.xlsx")
import json
for i in data['Sample Data'][1:]:
	#print i[0], i[1], i[2], i[3], i[4], i[5], i[6]
	q = Patient(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
	q.save()
