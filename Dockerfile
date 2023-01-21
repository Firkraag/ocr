FROM python:3.9
ADD . /ocr
WORKDIR /ocr
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
#echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list && \
#echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list && \
#echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list
# libgl1-mesa-glx is required by python package opencv
RUN apt update && apt install -y libgl1-mesa-glx tesseract-ocr
RUN pip install -r requirements.txt
RUN python manage.py migrate && python manage.py test
