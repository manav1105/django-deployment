from django.shortcuts import render

# Create your views here.
def index(request):
    cont_dict={'text':'hello world','number':22}
    return render(request,'basic_app/index.html',cont_dict)

def other(request):
    cont_dict={'text':'hello world','number':22}
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relativ_url.html')