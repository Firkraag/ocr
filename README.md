# About

a web service which can take an uploaded image and find any letters in it

# Run

Run the following command to launch the web service:

```bash
docker-compose up
```

then open [http://127.0.0.1:8000/recognization/](http://127.0.0.1:8000/recognization/)

# Test

Run the following command:

```bash
python manage.py test
```

The ocr test will evaluate the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between the actual string and the string we get from image. If the edit distance is less than one-tenth of the actual string, we consider it an successful ocr.

# Requirements

- pytesseract~=0.3.7: python wrap for [tesseract](https://github.com/tesseract-ocr/tesseract), an OCR package written in C++

- Pillow~=8.1.0

- Django~=3.1.5

- editdistance~=0.5.3: evaluate the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between the actual string and the string we get from image.

- opencv-python: preprocess the image, perform a threshold to segment the foreground from the background,

  or apply a median blur to reduce noise.