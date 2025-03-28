import logging
import logging.config
import os

import yaml

LOGGER_YAML_FILE = "logging.yml"


def custom_logging() -> logging.Logger:
    with open(LOGGER_YAML_FILE, "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    return logging.getLogger(os.getenv("ENV"))
