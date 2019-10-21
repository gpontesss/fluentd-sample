import http

from flask import Flask, request
from flask.wrappers import Response

from .loggers import exception_logger, method_logger, route_logger

app = Flask(__name__)

@app.route("/")
def root():
    resp = {"hello": "world"}
    return resp, http.HTTPStatus.OK


@app.route("/warning")
def warning():
    method_logger.warning(f"This is the warning route ({request.path})")
    return "", http.HTTPStatus.OK


@app.route("/exception")
def exception():
    e = EnvironmentError("Example expection")
    method_logger.debug(f"Throwing {e}")
    raise e


@app.before_request
def before_request():
    route_logger.debug(f"Acessing {request.method} {request.path}")


@app.errorhandler(404)
def handle_404(e: Exception):
    route_logger.debug(f"Tried to access path {request.path}, but it wasn't found")
    return "Page not found\n", http.HTTPStatus.NOT_FOUND


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    exception_logger.exception("An exception was caught!")
    return "An internal error occured\n", http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.after_request
def after_request(resp: Response):
    route_logger.debug(f'Returning "{resp}" as response for {request.path}')
    route_logger.info(
        f"\"{request.method} {request.path} {request.environ.get('SERVER_PROTOCOL')}\" {resp.status}"
    )
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
