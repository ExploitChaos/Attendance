import sqlite3

def read_data_from_table():
    db_file = 'dragonDB.db'

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Get the list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in the database.")
            return

        print("Tables available:")
        for i, table_tuple in enumerate(tables):
            print(f"{i+1}. {table_tuple[0]}")

        # Prompt the user to select a table
        try:
            table_choice = int(input("Enter the number of the table you want to read: ")) - 1
            if 0 <= table_choice < len(tables):
                table_name = tables[table_choice][0]
            else:
                print("Invalid choice.")
                return
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")
            return

        # Read all data from the selected table
        sql_query = f"SELECT * FROM {table_name}"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        
        # Get column names for better readability
        column_names = [description[0] for description in cursor.description]
        print(f"\nData in table '{table_name}':")
        print(column_names)
        print("-" * 30)
        
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    read_data_from_table()


def edit_data_in_table():
    db_file = 'dragonDB.db'

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Assume the table name is 'dragons' for this example
        table_name = 'dragons' 
        
        # Display the current data to the user
        print("Current data in the 'dragons' table:")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        print("-" * 30)
        for row in rows:
            print(row)

        # Get user input for the record and field to edit
        row_id_to_edit = input("\nEnter the ID of the record you want to edit: ")
        field_to_edit = input("Enter the name of the column you want to edit (e.g., 'name'): ")
        new_value = input(f"Enter the new value for '{field_to_edit}': ")

        # Construct the UPDATE query using parameters to prevent SQL injection
        sql_query = f"UPDATE {table_name} SET {field_to_edit} = ? WHERE id = ?"
        
        # Use a tuple for parameters
        params = (new_value, row_id_to_edit)
        
        # Execute the UPDATE statement
        cursor.execute(sql_query, params)
        conn.commit()
        
        print(f"\n✅ Successfully updated record with ID {row_id_to_edit}.")
        
    except sqlite3.Error as e:
        print(f"❌ An SQLite error occurred: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    edit_data_in_table()


def read_data(conn):
    cursor = conn.cursor()
    # Logic to read and display data (same as above)
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if not tables:
            print("No tables found.")
            return

        print("\nTables available:")
        for i, table_tuple in enumerate(tables):
            print(f"{i+1}. {table_tuple[0]}")
        
        choice = int(input("Select a table by number: ")) - 1
        table_name = tables[choice][0]

        cursor.execute(f"SELECT * FROM {table_name}")
        column_names = [description[0] for description in cursor.description]
        print(f"\nColumns: {column_names}")
        for row in cursor.fetchall():
            print(row)
    except (ValueError, IndexError, sqlite3.Error) as e:
        print(f"Error reading data: {e}")

def edit_data(conn):
    cursor = conn.cursor()
    # Logic to edit data (similar to above, with user input)
    try:
        table_name = input("Enter table name to edit: ")
        cursor.execute(f"SELECT * FROM {table_name}")
        column_names = [description[0] for description in cursor.description]
        print(f"Columns: {column_names}")
        print("Current data:")
        for row in cursor.fetchall():
            print(row)

        row_id = input("Enter the ID of the row to edit: ")
        column_name = input("Enter the name of the column to update: ")
        new_value = input("Enter the new value: ")

        sql = f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?"
        cursor.execute(sql, (new_value, row_id))
        conn.commit()
        print("Update successful!")

    except sqlite3.Error as e:
        print(f"Error editing data: {e}")
    
def main():
    db_file = 'dragonDB.db'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        while True:
            print("\n--- Database Menu ---")
            print("1. Read a table")
            print("2. Edit a table")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                read_data(conn)
            elif choice == '2':
                edit_data(conn)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()