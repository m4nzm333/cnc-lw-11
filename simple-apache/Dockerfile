FROM debian:stretch
# Update the repository sources list
RUN apt-get update
# Install and run apache
RUN apt-get install -y apache2 && apt-get clean
# Expose
EXPOSE 80
# Run at Background
CMD apachectl -D FOREGROUND
# Run sebagai detachble saja