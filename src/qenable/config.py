"""
Configuration Manager Module
Writes and reads configuration files in a globally canonical way.
"""
import os

import yaml

config_path = "conf"


def create_config_pipeline(name: str, config: dict) -> None:
    """
    Writes a pipeline config to file.
    :param name: Name of the pipeline
    :param config: Map of config items to be set
    """
    create_config(f"{config_path}/pipes", name, config)


def load_config_pipeline(name: str) -> dict:
    """
    Loads a pipeline config from file.
    :param name: Name of the pipeline
    :return: Map of config items
    """
    return load_config(f"{config_path}/pipes", name)


def create_config_general(config: dict) -> None:
    """
    Writes the general (global) config items to file.
    :param config: Map of general config items
    """
    create_config(f"{config_path}", "general", config)


def load_config_general() -> dict:
    """
    Loads the general (global) config from file
    :return: Map of general config items
    """
    return load_config(f"{config_path}", "general")


def create_config(path: str, name: str, config: dict) -> None:
    """
    (Over-)Writes a config file
    :param path: Path to config file
    :param name: Name of the config file
    :param config: Map of config items to be written
    """
    os.makedirs(path, exist_ok=True, mode=0o777)
    with open(f"{path}/{name}.yml", 'w', encoding="UTF-8") as file:
        file.write(yaml.dump(config, sort_keys=False))


def load_config(path: str, name: str) -> dict:
    """
    Loads a configuration from file.
    :param path: Path to config file
    :param name: Name of the config file
    :return: Map of config items
    """
    with open(f"{path}/{name}.yml", "r", encoding="UTF-8") as stream:
        return yaml.safe_load(stream)


def update_config(path: str, name: str, update: dict) -> None:
    """
    Updates a given configuration with the given values.
    Adds the items, if keys not existent, otherwise replaces the values.
    :param path: Path to config file
    :param name: Name of the config file
    :param update: Map of items to be updated
    """
    conf = load_config(path, name)
    conf.update(update)
    create_config(path, name, conf)


# Creates default general config, if not existent
if not os.path.exists(f"{config_path}/general.yml"):
    create_config_general(
        {
            "flask": {
                "TEMPLATES_AUTO_RELOAD": True,
            },
        })
