from DBFunctions import DBFunctions


def main():
    # Replace with your Neon DB credentials
    # Connect string from Neon:
    # postgresql://neondb_owner:npg_n1yXkw4aCoLV@ep-late-cloud-agqu0crh-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
    db_name = "neondb"
    user = "neondb_owner"
    password = "npg_n1yXkw4aCoLV"
    host = "ep-late-cloud-agqu0crh-pooler.c-2.eu-central-1.aws.neon.tech"
    port = "5432"  # Default PostgreSQL port

    # Initialize the DBFunctions object
    db = DBFunctions(db_name, user, password, host, port)

    # Connect to the database
    db.connect()

    # Execute a sample query
    query = "SELECT * FROM playing_with_neon;"
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
