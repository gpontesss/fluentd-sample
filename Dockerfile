FROM python:3.7.4-alpine

ENV APP_DIR /app
ENV APP_PORT 8080

WORKDIR ${APP_DIR}
COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY  . ${APP_DIR}

EXPOSE ${APP_PORT}

ENTRYPOINT [ "python" ]
CMD [ "-m", "fluentd_example" ]
