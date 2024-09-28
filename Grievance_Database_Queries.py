import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'raise_on_warnings': True
}

# Connect to MySQL server
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create database
    try:
        cursor.execute("CREATE DATABASE grievance_system;")
        print("Database 'grievance_system' created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'grievance_system' already exists.")
        else:
            print(err.msg)

    # Select the database
    cursor.execute("USE grievance_system;")
    
    # Create tables
    tables = {}

    tables['Users'] = (
        "CREATE TABLE Users ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  username VARCHAR(50) NOT NULL,"
        "  password VARCHAR(255) NOT NULL,"
        "  email VARCHAR(100) NOT NULL UNIQUE,"
        "  full_name VARCHAR(100),"
        "  course VARCHAR(100),"
        "  roll_number VARCHAR(100),"
        "  date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        ");"
    )

    tables['Course'] = (
        "CREATE TABLE Course ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  course_name VARCHAR(100) NOT NULL,"
        "  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        ");"
    )

    tables['Category'] = (
        "CREATE TABLE Category ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  category_name VARCHAR(100) NOT NULL,"
        "  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        ");"
    )

    tables['grievance'] = (
        "CREATE TABLE grievance ("
        "  grievance_id INT AUTO_INCREMENT PRIMARY KEY,"
        "  student_id INT,"
        "  course_id INT,"
        "  grievance_category_id INT,"
        "  room_number VARCHAR(50),"
        "  complaint TEXT,"
        "  status INT,"
        "  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        "  FOREIGN KEY (student_id) REFERENCES Users(id),"
        "  FOREIGN KEY (course_id) REFERENCES Course(id),"
        "  FOREIGN KEY (grievance_category_id) REFERENCES Category(id)"
        ");"
    )

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end='')
            cursor.execute(table_description)
            print("OK")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
    
    # Close cursor and connection
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
