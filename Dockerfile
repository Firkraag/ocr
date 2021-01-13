FROM python:3
ADD . /ocr
WORKDIR /ocr
# RUN apt install tesseract-ocr
# libgl1-mesa-glx is required by python package opencv
RUN apt update && apt install -y libgl1-mesa-glx tesseract-ocr
RUN pip install -v --default-timeout=100 -r requirements.txt
RUN python manage.py migrate
RUN python manage.py test
