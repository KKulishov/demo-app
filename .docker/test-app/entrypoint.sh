#!/bin/bash
set -e

if [[ ! -z "$1" ]]; then
    echo ${*}
    exec  ${*}
else
    exec /usr/local/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console --metrics_exporter none --service_name test-app flask run -h 0.0.0.0 -p 8080 
    #exec /usr/local/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console --metrics_exporter none --service_name demo-app flask run -h 0.0.0.0 -p 8080 
fi
