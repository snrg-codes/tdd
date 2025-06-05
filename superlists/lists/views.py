from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bosh_sahifa(request):
    if request.method == 'POST':
        iteam_text = request.POST['iteam-text']
        print(iteam_text)
        return HttpResponse(iteam_text)
    else:
        return render(request, 'bosh_sahifa.html')


