from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def convert_length(request):

    r1 = request.GET['rad1']
    return render(request, 'Convert_Length.html')