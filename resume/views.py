from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
  return render(request, "resume.html")

def download_pdf(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = BASE_DIR + '/files/Resume_Lorenzo_Mercado.pdf'
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the return value of the HttpResponse
    response = HttpResponse(path.read(), content_type='application/pdf')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=Resume_Lorenzo_Mercado.pdf"
    # Return the response value
    return response
