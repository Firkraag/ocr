import os

import editdistance
from django.conf import settings
from django.test import SimpleTestCase

from .ocr import ocr

examples_dir = os.path.join(settings.BASE_DIR, "examples")


# Create your tests here.
class OCRTest(SimpleTestCase):
    def test_ocr(self):
        image_files = [
            "example_01.webp",
            "example_02.png",
            "example_03.png",
            "example_04.png",
            "example_05.png",
        ]
        expected_results = [
            "Noisy image to test Tesseract OCR",
            "In order to manage memory more efficiently and with fewer errors, modern systems provide an abstraction of main memory known as virtual memory (VM).",
            "The default Vector2d.typecode is 'd',meaning each vector component will be repre-",
            "We are discussing adding a custom instance attribute, th",
            """The Python installers for the Windows platform usually include the entire standard library and often also
            include many additional components. For Unix-like operating systems Python is normally provided as a"""
        ]
        for image, expected_result in zip(image_files, expected_results):
            ocr_result = ' '.join(ocr(os.path.join(examples_dir, image)))
            distance = editdistance.eval(ocr_result, expected_result)
            self.assertTrue(distance * 10 < len(expected_result))
