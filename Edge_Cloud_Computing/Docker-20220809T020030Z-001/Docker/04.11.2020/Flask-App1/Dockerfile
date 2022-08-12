FROM python:3.8-alpine
LABEL maintainer="diot-feb-2020"
WORKDIR /usr/src/app
COPY application.py /usr/src/app
COPY requirements.txt /usr/src/app
#COPY . /usr/src/app
RUN pip3 install -r requirements.txt
EXPOSE 4500
CMD ["python3", "application.py"]