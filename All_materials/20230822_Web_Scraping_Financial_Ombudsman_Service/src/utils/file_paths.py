"""
Purpose of the script: loads config
"""
import logging

import toml

logger = logging.getLogger(__name__)


def get_config(toml_path="config.toml") -> dict:
    """Gets the config toml from the root directory and returns it as a dict. Can be called from any file in the project

    Returns:
        Dict: A dictionary containing details of the database, paths, etc. Should contain all the things that will change from one run to the next/

    """
    return toml.load(toml_path)
