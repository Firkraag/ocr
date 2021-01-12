from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def api_images(request: HttpRequest):
    # print(request.body)
    # file = request.FILES["image"]
    # print(request.FILES)
    return HttpResponse("success")


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "index.html", {})
