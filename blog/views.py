from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse



# Blog routes


#base for /blog
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")



#/blog/ . . .
def articles(request):
    return HttpResponse("Articles list")

def articlesByName(request, articleName):
    if len(articleName) <= 1:
        error = {"error": 1, "message": "something wrong happend !"}
        return JsonResponse(error)
    else:
        context = {'error': 0, 'message': articleName}
        return render(request, 'test1.html', context)


#basic test Post
@csrf_exempt #to try via postman, else error 403
def testPost(request):
    if(request.method == "POST"):
        return JsonResponse({'error': 0, 'message': request.POST.get("test", None)})
    else:
        return JsonResponse({'error': 1, 'message': 'Only post are allowed here !'})