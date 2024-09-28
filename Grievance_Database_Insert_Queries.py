import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # e.g., 'localhost'
    'database': 'grievance_system',
    'raise_on_warnings': True
}

# Connect to MySQL server
def add_user():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Insert data into Users table
        users_query = """
            INSERT INTO Users (username, password, email, full_name,course,roll_number,role) VALUES
            (%s, %s, %s, %s, %s, %s, %s)
            """
        users_data = [
            ('john_doe', 'password123', 'john3@example.com', 'John Doe', 'NA', 'NA', '1'),
            ('jane_smith', 'securepass', 'jane3@example.com', 'Jane Smith', 'B.tech', '12', '2'),
            ('alice_jones', 'mypassword', 'alice3@example.com', 'Alice Jones','B.tech', '14', '2')
        ]
        cursor.executemany(users_query, users_data)
        cnx.commit()
    except mysql.connector.Error as err:
        print("MySQL error :- ", err)

def add_course():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        # Insert data into Course table
        course_query = """
        INSERT INTO course(course_name) VALUES
        (%s)
        """
        course_data = [
            ('B.Tech',),
            ('M.Tech',),
            ('MCA',)
        ]
        cursor.executemany(course_query, course_data)
        cnx.commit()
    except mysql.connector.Error as err:
        print("MySQL error :- ", err)
"""add_course()"""

def add_category():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        # Insert data into Category table
        category_query = """
        INSERT INTO category(category_name) VALUES
        (%s)
        """
        category_data = [
            ('Water',),
            ('AC',),
            ('Bed',)
        ]
        cursor.executemany(category_query, category_data)
        cnx.commit()
    except mysql.connector.Error as err:
        print("MySQL error :- ", err)
"""add_category()"""

def add_grievance():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        # Insert data into grievance table
        grievance_query = """
        INSERT INTO grievance (student_id, course_id, grievance_category_id, room_number, complaint, status) VALUES
            (%s, %s, %s, %s, %s, %s)
            """
        grievance_data = [
            (1, 1, 1, 'Room 101', 'The course material is not accessible.', 1),
            (2, 2, 2, 'Room 202', 'Administrative staff are not helpful.', 1),
            (3, 3, 3, 'Room 303', 'The air conditioning is not working.', 1)
        ]
        cursor.executemany(grievance_query, grievance_data)
        cnx.commit()
    except mysql.connector.Error as err:
        print("MySQL error :- ", err)
add_grievance()
