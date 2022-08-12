#RUN A python application inside alpine with python installed
FROM python:3.8.6-alpine3.12
#MAINTAINER
LABEL maintainer="bhupendra.jmd@gmail.com"
#WORKDIR for container
WORKDIR /usr/src/app
#COPY the python from host to container
COPY displaymessage.py .
CMD ["python3", "displaymessage.py"] 
