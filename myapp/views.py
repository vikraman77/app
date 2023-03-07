from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse, FileResponse
from django.conf import settings
from wsgiref.util import FileWrapper
import re
import os


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['vikiadhi2016@gmail.com']
            if message:
                sender = ''
            send_mail(recipient_list=recipients, subject=f'New Mail from Your Portfolio Website!😀. Sender {email}', message=f'Hi vikram my name is, {name}\r\n \r\n Message:{message}', from_email='shieldgamer9444@gmail.com')

            return render(request, 'response.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skill(request):
    return render(request, 'skill.html')

# def navbar(request):
#     return render(request, 'navbar.html')

# def download_pdf(request):
#     with open('myapp/static/cv.pdf', 'rb') as f:
#         response = FileResponse(f, as_attachment=True, filename='cv.pdf')
#     return response


def download_pdf(request, filename):
    file_path = os.path.join('myapp', 'static', filename)
    file = open(file_path, 'rb')
    file_name = os.path.basename(file_path)
    response = HttpResponse(FileWrapper(file), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


def my_view(request):
    # Get the file name from the user somehow
    file_name = 'cv.pdf'
    response = download_pdf(request, file_name)
    return response