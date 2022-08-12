FROM gcc:10.2.0
LABEL organization="cdac"
WORKDIR /usr/docker/c-programming
COPY HelloWorld.c .
RUN gcc -o HelloWorld HelloWorld.c
CMD ["./HelloWorld"]
