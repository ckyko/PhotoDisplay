from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from base64 import b64encode

from .froms import UploadImageForm


def index(request):
    if request.method == "GET":
        data = {'image_form': UploadImageForm()}
        return render(request, 'core/index.html', data)
    if request.method == "POST":
        # image_form = UploadImageForm(request.POST, request.FILES)
        # print(request.FILES)

        myfile = request.FILES['image']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        # print(myfile.file)

        # print(dir(request))
        # print(request.FILES['image'])
        # image = request.FILES['image']
        # print(dir(image))
        # print(dir(image.file))

        image_data = myfile.read()
        # print(image_data)
        # im = image_data.decode('base64')
        # print(im)

        encoded = b64encode(image_data)
        # mime = "image/jpeg"
        # mime = mime + ";" if mime else ";"
        # input_image = "data:%sbase64,%s" % (mime, encoded)
        # print(input_image)

        return render(request, "core/show_image.html", {"input_image": encoded})

        # data = {'image': uploaded_file_url}

        # print(image_data)
        # if image_form.is_valid():
            # print(image_form)
            # print(image_form.image)
            # data = {'image': image_data}
            # data = {'image': request.FILES['image']}
            # print(request.FILES['image'])
            # handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('/success/url/')
            # return render(request, 'core/show_image.html', data)
        # return render(request, 'core/show_image.html', data)
        # return HttpResponse(image_data.decode('base64'), content_type='image/gif')



