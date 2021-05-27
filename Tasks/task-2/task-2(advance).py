import mysql.connector

mysqldb=mysql.connector.connect(host='localhost',user='root',password="root")
mycursor = mysqldb.cursor()
try:
    mycursor.execute('create database task2')
except:
    print('Database already exists')
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="task2")
    mycursor = mysqldb.cursor()
try:
    mycursor.execute("create table employee(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255), salary INT)")
except:
    print('table already exists')
def opt():
    print('choose option')
    print('1.insert data')
    print('2.read data')
    print('3.update data')
    print('4.delete data')
    print('5.exit')

    
    option = int(input('enter your choice:'))
    if option ==1:
        print("-----data inserting -----")
        name = input("enter name:")
        salary = input("enter salary:")
        
        ins_str = "insert into employee(name,salary) values('{}',{})".format(name,salary)
        try:
            print(ins_str)
            mycursor.execute(ins_str)
            mysqldb.commit()
            opt()
        except:
            mysqldb.rollback()
            print("failed to get data from Database")
            opt()
        mysqldb.close()
    elif option == 2:
        print('-----retrive data-----')
        try:
            mycursor.execute("select * from employee")
            data=mycursor.fetchall()
            print("id","name","salary")
            for i in data:
                print(i[0],i[1],i[2])
            print("----------------------")
            opt()
        except:
            print("failed to get data from Database")
            opt()    
    elif option == 3:
        print("-----Update Data------") 
        id = int(input('enter employee id to update'))
        print("select option for update:")
        print("1.update name")
        print("2.update salary")
        print("3.update both")
        op = input("enter update option:")
        if op == "1":
            print("----update name---")
            try:                
                name = input("enter new name :")
                update = "UPDATE employee SET name='{}' WHERE id={}".format(name,id)
                mycursor.execute(update)
                mysqldb.commit()
                opt()
            except:
                print("failed to update data from Database")
                opt()
        elif op == "2":
            try:
                print("----update salary---")   
                salary = int(input("enter new salary :"))
                update = "UPDATE employee SET salary={} WHERE id={}".format(salary,id)
                mycursor.execute(update)
                mysqldb.commit()
                opt()
            except:
                print("failed to update data from Database")
                opt()
        elif op == "3":
            try:
                print("----update both---")   
                name = input("enter new name:")
                salary = int(input("enter new salary :"))
                update = "UPDATE employee SET name='{}',salary={} WHERE id={}".format(name,salary,id)
                mycursor.execute(update)
                mysqldb.commit()
                opt()
            except:
                print("failed to update data from Database")
                opt()
    elif option== 4:
        id = input('Enter ID to be Deleted:')
        try:
            mycursor.execute("DELETE FROM employee WHERE id={}".format(id)) 
            mysqldb.commit()
            opt()
        except:
            mysqldb.rollback()
            opt()
        mysqldb.close()
    elif option== 4:
        exit()

opt()