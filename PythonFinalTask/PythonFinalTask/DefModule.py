import math
import pymysql
import sys

def connection():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful connection")
def sqlQuerryEveryThink():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM finaltask "
            cursor.execute(sql) 
            print()
            for row in cursor:
                print(row)       
    finally:
        # Закрыть соединение (Close connection).      
        connection.close()
def sqlAddProduct():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful category")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Category FROM finaltask "
            cursor.execute(sql) 
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
            print ("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)        
    finally:     
        connection.close()
def Hello():
    print ("Hello")
def ConversationtoCustomer():
    entYes=int(input("Вы хотите посмотреть весь ассортимент:нажмите 1 если согласны  или 2 если не согласны"))     
    if entYes==1:
            print("вывод данных")
    elif entYes==0:
            print("выводa данных нет")
    else:
             print("вы ввели неправильные данные")
def DetaSorted():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT * FROM finaltask ORDER BY Date DESC"
            cursor.execute(sql1)
            print ("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)        
    finally:     
        connection.close()
def PriceSorted():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='12345',                             
                                 db='python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT * FROM finaltask Order by Cost Desc"
            cursor.execute(sql1)
            print ("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)        
    finally:     
        connection.close()
def DeletePosition():
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
            #cursor.execute(sql1, (number))
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