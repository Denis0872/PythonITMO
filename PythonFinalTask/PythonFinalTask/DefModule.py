import math
import pymysql
import sys
import datetime


def connection(a):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
            with connection.cursor() as cursor:
                sql = str(a)
                cursor.execute(sql) 
                connection.commit()
                print()
                for row in cursor:
                    print(row)
    finally:
            connection.close()

def sqlQuerryEveryThink():
        a = "SELECT * FROM finaltask "
        connection(a)
  
def sqlAddCategory():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    Category=str(input("введите название категории"))
    Product=str(input("введите название товара"))
    Cost=str(input("введите цену"))
    Date= datetime.date.today()
    try:
       with connection.cursor() as cursor:
           sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( '{Category}', '{Product}', '{Cost}', '{Date}')".format(Category=Category,Product=Product,Cost=Cost,Date=Date)
           cursor.execute(sql) 
           connection.commit()
           print()
           for row in cursor:
                print(row)    
    finally:     
           connection.close()
def checkCon():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful!!")
 
    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT * FROM finaltask "
            cursor.execute(sql1)
            connection.commit()
            print ("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)        
    finally:     
        connection.close()
def Hello():
    print ("Hello")
def ConversationtoCustomerAddProduct():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    entYes=int(input("Вы хотите добавить продукт в существующую категорию, или создать новую? :нажмите 1 если выбираете существующую категорию  или 2 если нет"))     
    if entYes==1:
            sqlQuerryCategory()
            answer=str(input("выберите категорию   "))
            print()
            if answer=="Metall":
                print("вы выбрали металл ")
                Product=str(input("введите название товара "))
                Cost=str(input("введите цену "))
                Date= datetime.date.today()
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( 'Metall', '{Product}', '{Cost}', '{Date}')".format(Product=Product,Cost=Cost,Date=Date)
                        cursor.execute(sql) 
                        connection.commit()   
                finally:  
                    print("товар добавлен...")
                    connection.close()
            elif answer=="Technics":
                print("вы выбрали технику ")
                Product=str(input("введите название товара "))
                Cost=str(input("введите цену "))
                Date= datetime.date.today()
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( 'Technics', '{Product}', '{Cost}', '{Date}')".format(Product=Product,Cost=Cost,Date=Date)
                        cursor.execute(sql) 
                        connection.commit()    
                finally: 
                    print("товар добавлен...")
                    connection.close()
            elif answer=="Food":
                print("вы выбрали еду ")
                Product=str(input("введите название товара "))
                Cost=str(input("введите цену "))
                Date= datetime.date.today()
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( 'Food', '{Product}', '{Cost}', '{Date}')".format(Product=Product,Cost=Cost,Date=Date)
                        cursor.execute(sql) 
                        connection.commit()   
                finally: 
                    print("товар добавлен...")
                    connection.close()
            elif answer=="Wood":
                print("вы выбрали лесоматериалы ")
                Product=str(input("введите название товара "))
                Cost=str(input("введите цену "))
                Date= datetime.date.today()
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( 'Wood', '{Product}', '{Cost}', '{Date}')".format(Product=Product,Cost=Cost,Date=Date)
                        cursor.execute(sql) 
                        connection.commit()   
                finally: 
                    print("товар добавлен...")
                    connection.close()
            elif answer=="cars":
                print("вы выбрали автомобили ")
                Product=str(input("введите название товара "))
                Cost=str(input("введите цену "))
                Date= datetime.date.today()
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `finaltask` ( `Category`, `Product`, `Cost`, `Date`) VALUES ( 'cars', '{Product}', '{Cost}', '{Date}')".format(Product=Product,Cost=Cost,Date=Date)
                        cursor.execute(sql) 
                        connection.commit()
                finally: 
                    print("товар добавлен...")
                    connection.close()
            else:
                print("вы выбрали неправильно ")
    elif entYes==2:
            print("создайте категорию   ")
            sqlAddCategory()
    else:
             print("вы ввели неправильную цифру  ")

def DetaSorted():
    a="SELECT * FROM finaltask ORDER BY Date DESC"
    connection(a)
    
def PriceSorted():
    a = "SELECT * FROM finaltask Order by Cost Desc"
    connection(a)
def DeletePosition():

    sqlQuerryEveryThink()
    number=int(input("введите номер id строки,который вы хотите удалить")) 
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql1="Delete FROM finaltask Where id='%d'"% number
            cursor.execute(sql1)
            connection.commit()
            print()
            for row in cursor:
                print(row)        
    finally:     
        connection.close()
def ExitofProgramm(): 
  
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor) 
    connection.close()
def sqlQuerryCategory():
    a = " SELECT  DISTINCT Category FROM finaltask "
    connection(a)