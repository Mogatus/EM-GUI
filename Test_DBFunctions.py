from DBFunctions import DBFunctions
import configparser

def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    db = config["database"]

    db_name = db["database"]
    user = db["user"]
    password = db["password"]
    host = db["host"]
    port = db["port"]

    # Initialize the DBFunctions object
    db = DBFunctions(db_name, user, password, host, port)

    # Connect to the database
    db.connect()

    # Execute a sample query
    query = "SELECT * FROM meter_data;"
    result = db.execute_query(query)

    # Print the query result
    if result:
        print("Query Result:")
        for row in result:
            print(row)

    # Close the database connection
    db.close_connection()


# Call the main function
if __name__ == "__main__":
    main()
