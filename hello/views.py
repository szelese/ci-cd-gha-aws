from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, CI/CD GitHubActions, AWS! Minden rendben.", status=200)