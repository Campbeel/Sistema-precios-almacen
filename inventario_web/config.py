import os
from pathlib import Path


def _load_local_env():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_local_env()


def _get_env(name, default=""):
    return os.getenv(name, default)


class Config:
    SECRET_KEY = _get_env("FLASK_SECRET_KEY", "dev-secret-key")
    MYSQL_HOST = _get_env("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(_get_env("MYSQL_PORT", "3306"))
    MYSQL_USER = _get_env("MYSQL_USER", "almacen_app")
    MYSQL_PASSWORD = _get_env("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = _get_env("MYSQL_DATABASE", "almacen_interno")
