from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, CI/CD! It works.")