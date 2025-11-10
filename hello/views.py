from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, CI/CD GitHubActions, AWS! All OK!", status=200)

#Only for testing purposes/csak a tesztelés miatt
def cpu_test(request):
    try:
        count = 0
        for i in range(10**7):
            count += i
        return HttpResponse(f"CPU test OK. Count: {count}", status=200)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)