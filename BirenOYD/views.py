from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def convert_length(request):

    r1 = request.GET['rad1']
    r2 = request.GET['rad2']
    r3 = request.GET['rad3'] 
    if r1 == 'A':
        return render(request, 'Convert_Length.html',{'r1':r1,'r2':r2,'r3':r3})
    elif r1 == 'B':
        return render(request, 'Convert_Length2.html',{'r1':r1,'r2':r2,'r3':r3})
    else:
        return render(request, 'Convert_Length3.html',{'r1':r1,'r2':r2,'r3':r3})