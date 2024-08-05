import sqlite3
conn = sqlite3.connect("Employeezs.db",check_same_thread=False)

c = conn.cursor()
class UserClass:
  def __init__(self):
      pass
  def create_table(self):
      with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS employees(
        First_Name TEXT, 
        Last_Name TEXT,
        Phone_Number INTEGER,
        Date_Of_Joining DATE,
        Experience INTEGER,
        Designation TEXT,
        Salary INTEGER,
        Blood_Group TEXT,
        Email VARCHAR(200) PRIMARY KEY, 
        Password TEXT,
        User_Type TEXT)''')

  def insert_user(self,first_name,last_name,phone_number,doj,experience,desig,sal,blood,email,password,user_type):
      with conn:
        c.execute("INSERT INTO employees(First_Name, Last_Name,Phone_Number,Date_Of_Joining,Experience,Designation,Salary,Blood_Group,Email, Password,User_Type) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(first_name,last_name,phone_number,doj,experience,desig,sal,blood,email,password,user_type))

  def delete_User(self,email):
      with conn:
        c.execute(f"DELETE FROM employees WHERE Email = '{email}'")

  def existing_User(self,email):
      c.execute(f"SELECT * FROM employees WHERE Email = '{email}'")
      if c.fetchone() is None:
        return False
      else:
        return True

  def get_user(self,email):
    c.execute(f"SELECT Password FROM employees WHERE Email = '{email}'")
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None

  def get_user_details(self,email):
        c.execute(f"SELECT * FROM employees WHERE Email = '{email}'")
        result = c.fetchone()
        return result

  def get_user_type(self,email):
      c.execute(f"SELECT User_Type FROM employees WHERE Email = '{email}'")
      return c.fetchone()[0]
  def all_user(self):  
    c.execute("SELECT * FROM employees WHERE User_Type = 'Employee'")
    result = c.fetchall() 
    return result 

  def get_spec_emp(self,input):
      c.execute(f"SELECT * FROM employees WHERE First_Name = '{input}'")
      result = c.fetchall()
      return result

  def update_emp(self,email):
      c.execute(f"SELECT * FROM employees WHERE Email = '{email}'")
      result = c.fetchall()
      return result
  def save_changes(self,email, first_name, last_name, phone_number, date_of_joining, years_of_experience, designation, salary, blood_group):
      update_query = '''
        UPDATE employees
        SET First_Name = ?, Last_Name = ?, Phone_Number = ?, Date_Of_Joining = ?, Experience = ?, Designation = ?, Salary = ?, Blood_Group = ?
        WHERE Email = ?
        '''
      with conn:
          c.execute(update_query, (first_name, last_name, phone_number, date_of_joining, years_of_experience, designation, salary, blood_group, email))



c.execute("SELECT * FROM employees") 
print(c.fetchall())