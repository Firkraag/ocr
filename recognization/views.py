from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import OCR
from .ocr import ocr


# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def api_images(request: HttpRequest):
    file = request.FILES["image"]
    result = {
        'content': ocr(file.temporary_file_path()),
    }
    OCR.objects.create(image=file, result=result)
    return JsonResponse(result)


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "index.html", {})
