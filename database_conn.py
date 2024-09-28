import mysql.connector 

mydatabase = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "grievance"
)

cursor = mydatabase.cursor(buffered=True)
print("Connected Successfully")


def admin_logged(data):
    try :
        cursor.execute("SELECT * FROM `admin_db` WHERE username = %s AND password = %s",data)
        return cursor.fetchone()
    except Exception as e :
        print("Exception",e)
        return False
    
def user_logging(data):
    try :
        cursor.execute("SELECT * FROM `user_db` WHERE email = %s AND password = %s ",data)
        return cursor.fetchall()
    except Exception as e :
        print("Exception as ",e)
        return False


def user_register(data):
    try:
        cursor.execute('INSERT INTO `user_db`(`username`, `password`, `email`, `student_roll_no`) VALUES (%s,%s,%s,%s)', data)
        mydatabase.commit()
        return True
    except Exception as e:
        print("Exception",e)
        return False
    
def show_all_users():
    try:
        cursor.execute('SELECT * FROM `user_db`')
        return cursor.fetchall()
    except Exception as e:
        print("Exception is", e)
        return False
    
       
    
def updateStatus(data):
    try:
        print(data)
        cursor.execute('UPDATE `user_db` SET `status` = %s WHERE `id` = %s', data)
        mydatabase.commit()
        return True
    except Exception as e:
        print(e)
        return False    
    
def course():
    try:
        cursor.execute("SELECT * FROM `courses`")
        return cursor.fetchall()
    except Exception as e :
        print("Exception as ",e)
        return False

    
def categories():
    try:
        cursor.execute("SELECT * FROM `catagories`")
        return cursor.fetchall()
    except Exception as e :
        print("Exception as ",e)
        
def grievance_save(data):
    try:
        cursor.execute("INSERT INTO `grievance_model`(`student_id`,`course_id`, `categories_id`, `room_id`, `complaint`) VALUES (%s,%s,%s,%s,%s)",data)
        mydatabase.commit()
        return True
    except Exception as e :
        mydatabase.rollback()
        print("Exception as ",e)
        return False
    
    
def view_users_complaints():
    try:
        cursor.execute('SELECT * FROM `grievance_model`')
        return cursor.fetchall()
    except Exception as e:
        print("Exception is", e)
        return False

def changeStatus(data):
    try:
        print(data)
        cursor.execute('UPDATE `grievance_model` SET `status` = %s WHERE `id` = %s', data)
        mydatabase.commit()
        return True
    except Exception as e:
        print(e)
        return False 
    
    
def getSingleUser(id):
    try:
        print("id is here---------------",id)
        # print('SELECT * FROM `grievance_model` WHERE `student_id` = %s', id)
        cursor.execute('SELECT * FROM `grievance_model` WHERE `student_id` = %s', (id,))
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
def view_all_courses():
    try:
        cursor.execute('SELECT * FROM `courses`')
        return cursor.fetchall()
    except Exception as e:
        print("Exception is", e)
        return False
    
def insert_all_courses(course_name):
    try:
        cursor.execute("INSERT INTO `courses`(`course_name`) VALUES (%s)",(course_name,))
        mydatabase.commit()
        return True
    except Exception as e :
        mydatabase.rollback()
        print("Exception as ",e)
        return False
def update_all_courses(id,data):
    try :
        cursor.execute("UPDATE `courses` SET `course_name`= %s WHERE id=%s",(data,id))
        mydatabase.commit()
        return True
    except Exception as e:
        print(e)
        return False
def delete_all_courses(id):
    try :
        cursor.execute('DELETE FROM `courses` WHERE id=%s',(id,))
        mydatabase.commit()
        return True
    except Exception as e :
        print("Exception as e",e)
        
def view_all_category():
    try:
        cursor.execute('SELECT * FROM `catagories`')
        return cursor.fetchall()
    except Exception as e:
        print("Exception is", e)
        return False
    
def delete_all_category(id):
    try :
        cursor.execute('DELETE FROM `catagories` WHERE id=%s',(id,))
        mydatabase.commit()
        return True
    except Exception as e :
        print("Exception as e",e)
        
def insert_all_category(category_name):
    try:
        cursor.execute("INSERT INTO `catagories`(`categories_name`) VALUES (%s)",(category_name,))
        mydatabase.commit()
        return True
    except Exception as e :
        mydatabase.rollback()
        print("Exception as ",e)
        return False
    
def update_all_category(id,data):
    try :
        cursor.execute("UPDATE `catagories` SET `categories_name`= %s WHERE id=%s",(data,id))
        mydatabase.commit()
        return True
    except Exception as e:
        print(e)
        return False
