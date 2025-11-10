from django.http import HttpResponse
import hashlib

def index(request):
    return HttpResponse("Hello, CI/CD GitHubActions, AWS! All OK!", status=200)

#Only for testing purposes/csak a tesztelés miatt
def cpu_test(request):
    try:
        text_to_hash=b"CPU test"
        iterations = 100000
        for i in range(iterations):
            text_to_hash = hashlib.sha256(text_to_hash).digest()    
        return HttpResponse(f"CPU test OK. Completed {iterations} hash iterations.", status=200)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)