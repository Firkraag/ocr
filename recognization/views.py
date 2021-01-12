from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .ocr import ocr


# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def api_images(request: HttpRequest):
    file = request.FILES["image"]
    return HttpResponse(ocr(file.temporary_file_path()))


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "index.html", {})
