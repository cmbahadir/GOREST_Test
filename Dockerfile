FROM selenium/standalone-chrome:3.5.3
MAINTAINER cmbahadir

USER root

ADD /Gorest-Test/API_Test/userlist.py /home/seluser/userlist.py

RUN apt-get -y update && apt-get install -y --no-install-recommends curl inetutils-ping && \
    apt-get install -y --no-install-recommends python3 pip3 && \
    chmod 777 /home/seluser/* && \

    pip install selenium==3.3.1 && \
    apt-get -y remove && apt-get -y autoremove && rm -rf /var/cache/apk/* && \

    which curl && which ping && \
    python --version 2>&1 | grep 2.7.12 && \
    pip --version | grep 8.1.1 && \
    pip list | grep selenium.*3.3.1 && \
    cksum /opt/selenium/selenium-server-standalone.jar | grep 46755906

USER seluser

WORKDIR /home/seluser
