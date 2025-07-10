import requests
from django.shortcuts import render,redirect,HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import LandRecord
from .serializers import LandRecordSerializer

def upload_area(request):
    return render(request, 'upload_land_record.html')

@api_view(['POST'])
def upload_land_record_form(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('photo')

        LandRecord.objects.create(
            full_name=data.get('full_name'),
            mandal=data.get('mandal'),
            district=data.get('district'),
            state=data.get('state'),
            aadhar_number=data.get('aadhar_number'),
            document_number=data.get('document_number'),
            survey_number=data.get('survey_number'),
            photo=image
        )
        return redirect('upload_success')  # Optional: make a success page

    return render(request, 'upload_land_record.html')
@api_view(['POST'])
def check_land_record_with_api(request):
    aadhar_number = request.data.get('aadhar_number')
    document_number = request.data.get('document_number')
    survey_number = request.data.get('survey_number')
    new_image = request.FILES.get('photo')

    if not all([aadhar_number, document_number, survey_number, new_image]):
        return Response({'error': 'All fields are required.'}, status=400)

    try:
        record = LandRecord.objects.get(aadhar_number=aadhar_number)
    except LandRecord.DoesNotExist:
        return Response({'error': 'Record not found.'}, status=404)

    if record.document_number != document_number or record.survey_number != survey_number:
        return Response({'error': 'Document or survey number mismatch.'}, status=400)

    try:
        # Prepare files for API (new photo and stored photo)
        stored_photo_url = record.photo.url
        files = {
            'image1': requests.get(stored_photo_url, stream=True).raw,
            'image2': new_image,
        }

        # Replace with your API endpoint
        api_url = 'https://your-facerec-api.com/compare'
        headers = {'Authorization': 'Bearer YOUR_API_KEY'}

        response = requests.post(api_url, files=files, headers=headers)
        result = response.json()

        if result.get('match', False):
            return Response({'status': 'verified'})
        else:
            return Response({'status': 'image not matched'})

    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
def upload_success(request):
    return HttpResponse("<h2>Record uploaded successfully!</h2>")

@api_view(['GET'])
def all_land_records_view(request):
    records = LandRecord.objects.all()
    return render(request, 'all_land_records.html', {'records': records})