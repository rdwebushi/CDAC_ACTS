FROM python:3.8-alpine
LABEL maintainer="diot-feb-2020"
WORKDIR /usr/src/app
#Add all the files of source directory to /usr/src/app
COPY . .                    
RUN pip3 install -r requirements.txt
EXPOSE 4500
CMD ["python3", "application.py"]

