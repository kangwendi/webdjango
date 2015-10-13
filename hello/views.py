from django.shortcuts import render

# Create your views here.

def hello(request):
    variabels = {
        'key': "Hello World"
    }
    return render(request, 'hello/hello.html', variabels)

def save(request):
    pass

def edit(request):
    pass
