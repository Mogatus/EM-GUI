import configparser
from pathlib import Path

import pytest

from DBFunctions import DBFunctions


@pytest.fixture(scope="module")
def db_config():
    config_path = Path("config.ini")
    if not config_path.exists():
        pytest.skip("config.ini fehlt: DB-Integrationstest wird übersprungen.")

    parser = configparser.ConfigParser()
    parser.read(config_path)

    if "database" not in parser:
        pytest.skip("[database]-Abschnitt fehlt in config.ini.")

    db = parser["database"]
    required_keys = ["database", "user", "password", "host", "port"]
    missing = [key for key in required_keys if not db.get(key)]
    if missing:
        pytest.skip(f"DB-Konfiguration unvollständig, fehlend: {', '.join(missing)}")

    return {
        "db_name": db["database"],
        "user": db["user"],
        "password": db["password"],
        "host": db["host"],
        "port": db["port"],
    }


def test_execute_select_query_returns_rows_or_empty(db_config):
    db = DBFunctions(
        db_config["db_name"],
        db_config["user"],
        db_config["password"],
        db_config["host"],
        db_config["port"],
    )

    db.connect()
    if not db.connection:
        pytest.skip("DB nicht erreichbar: Integrationstest wird übersprungen.")

    try:
        result = db.execute_query("SELECT * FROM meter_data;")
    finally:
        db.close_connection()

    assert result is None or isinstance(result, list)

