import math
from data import MENU,resources
print("Cofee Machine !")
print(f'''
Resources Available      

Water : {resources["water"] }  ml
Milk : {resources["milk"]}  ml 
Cofee Powder : {resources["coffee"]}  grams

''')
print("Menu Card !")
print(f'''
      
Espresso : Ingredients = {MENU["espresso"]["ingredients"]} , Cost = ${MENU["espresso"]["cost"]}

Latte : Ingredients = {MENU["latte"]["ingredients"]} , Cost = ${MENU["latte"]["cost"]}

Cappuccino : Ingredients = {MENU["cappuccino"]["ingredients"]} , Cost = ${MENU["cappuccino"]["cost"]}
''')
print('''
Coins Operated !

Penny : 1 cent 
Dime : 10 cents                   
Nickel : 5 cents
Quarter : 25 cents                  
      
''')
print('''
      Type
1.Resources - For details of stock of resources
2.Exit - To exit Coffee Machine            
''')

def cofee_machine():
        choice = input("Enter your Order ").lower()
        cost_of_drink = MENU[choice]["cost"]
        print('''
         Enter Money in the given types
           ''')
        penny = int(input("Enter Pennys :  "))
        dime = int(input("Enter Dime : "))
        quarter = int(input("Enter Quarter : "))
        nickel = int(input("Enter nickel :  "))
        user_money = round(penny*1/100 + dime*10/100 + nickel*5/100 + quarter*25/100,1) 
        print(f" User Money : ${user_money} , Cost = ${cost_of_drink}")

        if cost_of_drink <= user_money:
             print(f'''
             Thank you for your Order !
             your change : {round(float(user_money) - float(MENU[choice]["cost"]),2)}      
             Come and Get fucked Again !
             ''')
        else:
               print("Not enough money")
               print(f"You need : ${cost_of_drink - user_money}")
            
        details = input("What u need to know ?").lower()
        if details == "resources":
               if choice == "espresso":
                         remain_coffee =int(resources["coffee"]) - int(MENU[choice]["ingredients"]["coffee"])
                         remain_water = int(resources["water"]) - int(MENU[choice]["ingredients"]["water"]) 
                         print(f"Water : {remain_water}, Coffee : {remain_coffee}, Milk :{resources['milk']} " )
                         cofee_machine()
               elif choice == "cappuccino" or choice == "latte":    
                        remain_water = int(resources["water"]) - int(MENU[choice]["ingredients"]["water"]) 
                        remain_milk = int(resources["milk"]) - int(MENU[choice]["ingredients"]["milk"])
                        remain_coffee = int(resources["coffee"]) - int(MENU[choice]["ingredients"]["coffee"])
                        print(f"Water : {remain_water}, Milk :{remain_milk}, Coffee : {remain_coffee}  " )
                        cofee_machine() 
        elif details == "exit":
                print("Thank you come again !")
                return
cofee_machine()    
                                         
