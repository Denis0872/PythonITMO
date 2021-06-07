import DefModule
import sys

#DefModule.checkCon()
DefModule.Hello()
#DefModule.connection()
#DefModule.sqlQuerryCategory()
#DefModule.ConversationtoCustomer()
#DefModule.sqlQuerryEveryThink

entYes1=int(input("Выберите что вы хотите вывести. цифры от 1 до 6. 1-добавить продукт,2-показать все продукты,3-отсортировать всё по дате,4-отсортировать по цене,5-удалить продукт,6-выйти "))     
if entYes1==1:
     DefModule.sqlAddProduct()
elif entYes1==2:
    DefModule.sqlQuerryEveryThink()
elif entYes1==3:
    DefModule.DetaSorted();
elif entYes1==4:
    DefModule.PriceSorted();
elif entYes1==5:
    DefModule.DeletePosition();
elif entYes1==6:
    DefModule.ExitofProgramm()
else:
    print("вы ввели неправильную цифру. Попробуйте снова")