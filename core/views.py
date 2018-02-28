from django.shortcuts import render
from django.http import HttpResponse
from base64 import b64encode

from .froms import UploadImageForm


def index(request):
    if request.method == "GET":
        data = {'image_form': UploadImageForm()}
        return render(request, 'core/index.html', data)
    else:
        return HttpResponse("method not allowed.", status=405)


def image(request):
    if request.method == "POST":
        if 'image' not in request.FILES:
            return HttpResponse("Bad request. Please post a image file.", status=400)
        image_file = request.FILES['image']
        image_data = image_file.read()
        encoded = b64encode(image_data)
        return render(request, "core/show_image.html", {"input_image": encoded})
    else:
        return HttpResponse("method not allowed.", status=405)
