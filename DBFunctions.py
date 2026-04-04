import psycopg2
from psycopg2 import OperationalError
from datetime import date, datetime


def _parse_timestamp(value):
    """Convert supported timestamp values to datetime."""
    if isinstance(value, datetime):
        return value

    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())

    if isinstance(value, str):
        timestamp_value = value.strip()
        if timestamp_value.endswith("Z"):
            timestamp_value = f"{timestamp_value[:-1]}+00:00"

        try:
            return datetime.fromisoformat(timestamp_value)
        except ValueError:
            for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d"):
                try:
                    return datetime.strptime(timestamp_value, fmt)
                except ValueError:
                    continue

    raise ValueError(f"Unsupported timestamp value: {value!r}")


def keep_latest_entry_per_day(data, timestamp_index=-1):
    """Return same container type with only the latest row per calendar day."""
    if data is None:
        return None

    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple of rows")

    latest_by_day = {}
    for row_index, row in enumerate(data):
        timestamp = _parse_timestamp(row[timestamp_index])
        day = timestamp.date()
        current = latest_by_day.get(day)

        # Prefer newer timestamps; if equal, keep the last occurrence.
        if current is None or timestamp > current[0] or (timestamp == current[0] and row_index > current[1]):
            latest_by_day[day] = (timestamp, row_index, row)

    filtered_rows = [latest_by_day[day][2] for day in sorted(latest_by_day)]
    return tuple(filtered_rows) if isinstance(data, tuple) else filtered_rows


class DBFunctions:
    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Establish a connection to the Neon database."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connection to the database established successfully.")
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        """
        Execute a SQL query on the Neon database.
        :param query: SQL query string
        :param params: Optional parameters for the query
        :return: Query result or None
        """
        if not self.connection:
            print("No active database connection.")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if query.strip().lower().startswith("select"):
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
                    print("Query executed successfully.")
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        else:
            print("No active connection to close.")
