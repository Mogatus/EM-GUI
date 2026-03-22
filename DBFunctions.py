import psycopg2
from psycopg2 import OperationalError


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
