
FROM docker.io/istio/examples-bookinfo-productpage-v1:1.17.0

#ENV HTTPS_PROXY http://proxy-server.sovcombank.group:3128
#ENV HTTP_PROXY http://proxy-server.sovcombank.group:3128
#ENV https_proxy http://proxy-server.sovcombank.group:3128
#ENV http_proxy http://proxy-server.sovcombank.group:3128
#ENV NO_PROXY "127.0.0.1,localhost,.sovcombank.group,minio,.sovcombank.ru,.svc.cluster.local"

USER root

RUN groupadd -g 1000 python
RUN useradd -s /bin/bash -g python -u 1000 -g 1000 python

WORKDIR /opt/microservices

#RUN pip3 install opentelemetry-distro opentelemetry-exporter-otlp && opentelemetry-bootstrap -a install
COPY .docker/productpage/requirements.txt /opt/microservices/
RUN pip install -r requirements.txt

COPY .docker/productpage/lib /opt/microservices/lib/
COPY .docker/productpage/productpage.py /opt/microservices/

RUN chown -R 1000:1000 /opt/microservices

COPY .docker/productpage/entrypoint.sh /opt/microservices/entrypoint.sh 

RUN chown -R 1000:1000 /opt/microservices/entrypoint.sh && chmod +x /opt/microservices/entrypoint.sh

ENTRYPOINT ["/opt/microservices/entrypoint.sh"]

USER 1000
