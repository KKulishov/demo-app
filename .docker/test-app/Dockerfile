FROM python:3-buster

RUN ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone

#ENV HTTPS_PROXY http://proxy-server.sovcombank.group:3128
#ENV HTTP_PROXY http://proxy-server.sovcombank.group:3128
#ENV https_proxy http://proxy-server.sovcombank.group:3128
#ENV http_proxy http://proxy-server.sovcombank.group:3128
#ENV NO_PROXY "127.0.0.1,localhost,.sovcombank.group,minio,.sovcombank.ru,coroot-clickhouse,.coroot,coroot-opentelemetry-collector.coroot,.coroot.svc.cluster.local"

USER root

RUN groupadd -g 1000 python
RUN useradd -s /bin/bash -g python -u 1000 -g 1000 python

RUN mkdir -p /app/lib 

WORKDIR /app/lib

#RUN apt update && apt install -y python3-dev && apt install -y build-essential

RUN pip install flask opentelemetry-distro opentelemetry-exporter-otlp opentelemetry-instrumentation-flask && opentelemetry-bootstrap -a install

COPY .docker/test-app/*.py /app/lib/

COPY .docker/test-app/entrypoint.sh /app/lib/

RUN chown -R python:python /app

ENTRYPOINT [ "opentelemetry-instrument", "python", "app.py" ]
#ENTRYPOINT ["/app/lib/entrypoint.sh"]

USER python
