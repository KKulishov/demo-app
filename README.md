### Demo app 

примеры кода 
[src](https://github.com/istio/istio/tree/master/samples/bookinfo)
[istio_docs](https://istio.io/latest/docs/setup/getting-started/)



ручной 
https://coroot.com/docs/coroot-community-edition/tracing/opentelemetry-python
https://opentelemetry.io/docs/instrumentation/python/

python + java + ruby + js 

redis + mysql

auto  → kuber operator 
https://opentelemetry.io/docs/kubernetes/operator/automatic/

оператор как зависмоть просить issue certmanager



ДЛя ns coroot разрешить вх. трафик для OTEL от ns  bookinfo 

точки генерации траффика
https://bookinfo-k8s-test.sovcombank.group/index.html
https://bookinfo-k8s-test.sovcombank.group/productpage
https://bookinfo-k8s-test.sovcombank.group/api/v1/products/82344/reviews
https://bookinfo-k8s-test.sovcombank.group/api/v1/products/32
https://bookinfo-k8s-test.sovcombank.group/api/v1/products/82344/ratings
## redis
https://bookinfo-k8s-test.sovcombank.group/redis-write
https://bookinfo-k8s-test.sovcombank.group/redis-read
## mysql 
https://bookinfo-k8s-test.sovcombank.group/mysql-set
https://bookinfo-k8s-test.sovcombank.group/mysql-read


## todo add postgesql

## todo add proxysql

## todo тупикоый сервис к которому обращается сервис но он не отвечает 


## primer 
https://github.com/open-telemetry/opentelemetry-demo/blob/main/src/recommendationservice/Dockerfile
https://github.com/open-telemetry/opentelemetry-demo/tree/main
https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-flask

https://opentelemetry.io/docs/instrumentation/python/automatic/agent-config/
https://opentelemetry.io/docs/instrumentation/python/automatic/

https://scoutapm.com/blog/configuring-opentelemetry-python
## operator
https://opentelemetry.io/docs/kubernetes/operator/
https://www.infracloud.io/blogs/opentelemetry-auto-instrumentation-jaeger/