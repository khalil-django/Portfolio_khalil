from django.shortcuts import render
from django.http import HttpResponse


import os
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Upload

# Create your views here.

def mainPage(request):
    files = Upload.objects.all()
    context = {
        'files': files
        }
    
    # return HttpResponse("Welcome to django portfolio!!!")
    return render(request, 'portfolio/main.html', context)

def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404