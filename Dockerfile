FROM selenium/standalone-chrome:3.5.3
MAINTAINER cmbahadir

USER root

COPY . /home/seluser/Gorest-Test

CMD apt-get -y update && apt-get install -y --no-install-recommends curl inetutils-ping
CMD apt-get install -y --no-install-recommends python3 pip3
CMD chmod 777 /Gorest-Test *
CMD cd /home/seluser/Gorest-Test && pip3 install -r requirements.txt

USER seluser

WORKDIR /home/seluser
