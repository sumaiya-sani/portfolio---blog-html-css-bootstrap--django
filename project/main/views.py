from fileinput import filename
from importlib.resources import contents
from urllib import response
from django.forms import FilePathField
from django.shortcuts import render
import mimetypes
import os
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.http.response import HttpResponse


def home(request):

    return render(request,'home.html')


def article_details(request):

    return render(request,'article_details.html')

def my_cv(request):
    return render(request,'cv.html')


#downoload

  # Define function to download pdf file using template
def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/main/files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'cv.html')









 