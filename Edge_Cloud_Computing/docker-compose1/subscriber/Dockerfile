FROM python:3.7
LABEL maintainer="diotfeb2020"
WORKDIR /usr/src/app/
COPY subscriber-mqtt.py /usr/src/app/
COPY req.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r req.txt
CMD ["python", "subscriber-mqtt.py"]
