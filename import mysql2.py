import mysql.connector
name=str(input("Enter name of customer table"))
address=str(input("Enter address of customer table"))
name_1=str(input("Enter name of customers_students table"))
address_2=str(input("Enter address of customers_students table"))
email=str(input("Enter email of customers_students table"))
gender=str(input("Enter gender of customers_students table"))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit_ece"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = (name, address)
mycursor.execute(sql, val)

sql_2 = "INSERT INTO customers_students (name, address,email,gender) VALUES (%s, %s,%s,%s)"
val_2 = (name_1,address_2,email,gender)
mycursor.execute(sql_2, val_2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")