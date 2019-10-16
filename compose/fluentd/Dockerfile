# Refer to https://hub.docker.com/r/fluent/fluentd/
FROM fluent/fluentd:v1.7.3-1.0

USER root

RUN fluent-gem install fluent-plugin-elasticsearch

USER fluent
