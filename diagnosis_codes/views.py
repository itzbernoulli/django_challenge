from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DiagnosisCode
from .serializers import DiagnosisCodeSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(['GET','DELETE','PUT'])
def get_delete_update_diagnosis_code(request, pk):
	try:
		diagnosis = DiagnosisCode.objects.get(pk=pk)
	except DiagnosisCode.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	#get details of a single diagnosis
	if request.method == 'GET':
		serializer = DiagnosisCodeSerializer(diagnosis)
		return Response(serializer.data)
	#delete a single diagnosis
	if request.method == 'DELETE':
		diagnosis.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	#update details of a single diagnosis
	if request.method == 'PUT':
		serializer = DiagnosisCodeSerializer(diagnosis, data = request.data)
		if serializer.is_valid():
			serializer.save
			return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_post_diagnosis(request):
	#get all diagnosis
	if request.method == 'GET':
		paginator = PageNumberPagination()
		paginator.page_size = 20
		diagnosis = DiagnosisCode.objects.all()
		result_page = paginator.paginate_queryset(diagnosis, request)
		serializer = DiagnosisCodeSerializer(result_page,many=True)
		return paginator.get_paginated_response(serializer.data)
	#insert a new record for a diagnosis
	elif request.method == 'POST':
		data = {
			'category_code' : request.data.get('category_code'),
			'diagnosis_code' : request.data.get('diagnosis_code'),
			'full_code' : request.data.get('full_code'),
			'abbreviated_description' : request.data.get('abbreviated_description'),
			'full_description' : request.data.get('full_description'),
			'category_title' : request.data.get('category_title')
		}

		serializer = DiagnosisCodeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
