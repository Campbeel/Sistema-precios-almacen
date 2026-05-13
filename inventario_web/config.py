import os


def _get_env(name, default=""):
    return os.getenv(name, default)


class Config:
    SECRET_KEY = _get_env("FLASK_SECRET_KEY", "dev-secret-key")
    MYSQL_HOST = _get_env("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(_get_env("MYSQL_PORT", "3306"))
    MYSQL_USER = _get_env("MYSQL_USER", "root")
    MYSQL_PASSWORD = _get_env("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = _get_env("MYSQL_DATABASE", "almacen_interno")
