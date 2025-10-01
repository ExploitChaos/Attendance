import sqlite3

def create_table_in_dragon_db():
    """
    Connects to the 'dragonDB.db' database, prompts the user for a table name,
    and creates a new table with that name.
    """
    # Specify the name of your existing database file
    db_file = 'dragonDB.db'

    try:
        # Connect to your specific SQLite database file
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Prompt the user for the table name
        table_name = input("Enter the name for the new table in dragonDB.db: ")

        # Check if the input is valid
        if not table_name.strip():
            print("Error: Table name cannot be empty.")
            return

        # Use an f-string to insert the user's table name into the SQL query.
        # This is necessary because SQLite's parameter substitution doesn't work for table names.
        sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT)"

        # Execute the SQL command
        cursor.execute(sql_query)

        # Commit the changes to the database
        conn.commit()
        print(f"✅ Table '{table_name}' created successfully in {db_file}")

    except sqlite3.Error as e:
        # Catch any SQLite-related errors
        print(f"❌ An SQLite error occurred: {e}")
    finally:
        # Always close the connection
        if conn:
            conn.close()
            print("Connection to the database closed.")

if __name__ == "__main__":
    create_table_in_dragon_db()