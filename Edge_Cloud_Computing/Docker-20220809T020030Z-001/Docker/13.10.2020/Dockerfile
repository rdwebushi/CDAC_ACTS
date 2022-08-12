FROM centos:7

LABEL developer="diot-2020"

RUN yum -y update httpd

RUN yum -y install httpd

COPY index.html /var/www/html

COPY IoT.png /var/www/html
#start your process (httpd) with systemd in FOREGROUND ensuring to start the
#server by systemd if it crashes in between 
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

#Run the server at port 80 inside container

EXPOSE 80  
