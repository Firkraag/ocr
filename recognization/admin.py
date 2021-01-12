from django.contrib import admin

from .models import OCR


class OCRAdmin(admin.ModelAdmin):
    list_display = ('image', 'result')


admin.site.register(OCR, OCRAdmin)
