import logging
import logging.config
import os
import os.path
import sys

import yaml

with open(os.getenv("LOG_CONFIG_FILE"), "r") as yaml_file:
    config = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)

route_logger = logging.getLogger("app.route")
method_logger = logging.getLogger("app.method")
exception_logger = logging.getLogger("app.exception")

logging.config.dictConfig(config)
