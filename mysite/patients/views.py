from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Patient

from django.views import generic

from django.db import models

from chartit import DataPool, Chart

def index(request):
	patientList = Patient.objects.all()
	#print Patient.objects.all().count()

	#filter by ID
	myPatientID = request.GET.get('myPatientID')
	if myPatientID:
		patientList = patientList.filter(pk=myPatientID)

	# filter by PSA
	myMinPSA = request.GET.get('myMinPSA')
	myMaxPSA = request.GET.get('myMaxPSA')
	if myMinPSA:
		patientList = patientList.filter(PSA__gte = myMinPSA)
	if myMaxPSA:
		patientList = patientList.filter(PSA__lte = myMaxPSA)

	# filter by Prostate Vol
	myMinProstateVol = request.GET.get('myMinProstateVol')
	myMaxProstateVol = request.GET.get('myMaxProstateVol')
	if myMinProstateVol:
		patientList = patientList.filter(prostate_vol__gte = myMinProstateVol)
	if myMaxProstateVol:
		patientList = patientList.filter(prostate_vol__lte = myMaxProstateVol)

	# filter by Lesion size
	myMinLesionSize = request.GET.get('myMinLesionSize')
	myMaxLesionSize = request.GET.get('myMaxLesionSize')
	if myMinLesionSize:
		patientList = patientList.filter(lesion_size__gte = myMinLesionSize)
	if myMaxLesionSize:
		patientList = patientList.filter(lesion_size__lte = myMaxLesionSize)

	# filter by Sector
	myMinSector = request.GET.get('myMinSector')
	myMaxSector = request.GET.get('myMaxSector')
	if myMinSector:
		patientList = patientList.filter(sector__gte = myMinSector)
	if myMaxSector:
		patientList = patientList.filter(sector__lte = myMaxSector)

	# filter by PIRADS score
	myMinPIRADSscore = request.GET.get('myMinPIRADSscore')
	myMaxPIRADSscore = request.GET.get('myMaxPIRADSscore')
	if myMinPIRADSscore:
		patientList = patientList.filter(PIRADS_score__gte = myMinPIRADSscore)
	if myMaxPIRADSscore:
		patientList = patientList.filter(PIRADS_score__lte = myMaxPIRADSscore)

	# filter by GLEASON score
	myMinGLEASONscore = request.GET.get('myMinGLEASONscore')
	myMaxGLEASONscore = request.GET.get('myMaxGLEASONscore')
	if myMinGLEASONscore:
		patientList = patientList.filter(GLEASON_score__gte = myMinGLEASONscore)
	if myMaxGLEASONscore:
		patientList = patientList.filter(GLEASON_score__lte = myMaxGLEASONscore)

	# Get sector-count list 
	sectorList = []
	for i in range(1, 39):
		if patientList.filter(sector=i).count():
			sectorList.append([i, patientList.filter(sector=i).count()])
	#print sectorList

	context = {
		'patientList': patientList,
		'myMinPSA': myMinPSA,
		'myMaxPSA': myMaxPSA,
		'myMinProstateVol': myMinProstateVol,
		'myMaxProstateVol': myMaxProstateVol,
		'myMinLesionSize': myMinLesionSize,
		'myMaxLesionSize': myMaxLesionSize,
		'myMinSector': myMinSector,
		'myMaxSector': myMaxSector,
		'myMinPIRADSscore': myMinPIRADSscore,
		'myMaxPIRADSscore': myMaxPIRADSscore,
		'myMinGLEASONscore': myMinGLEASONscore,
		'myMaxGLEASONscore': myMaxGLEASONscore,
		'sectorList': sectorList,
	
	}
	return render(request, 'patients/index.html', context)

class DetailView(generic.DetailView):
	model = Patient
	template_name = 'patients/detail.html'
