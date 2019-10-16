import logging
import logging.config
import os
import os.path
import sys

import yaml

with open(os.getenv("LOG_CONFIG_FILE"), "r") as yaml_file:
    config = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)

logging.config.dictConfig(config)

route_logger = logging.getLogger("route")
method_logger = logging.getLogger("method")
exception_logger = logging.getLogger("exception")
