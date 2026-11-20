import random

comp_numb = random.randint(1,100) #ранд

is_run=True #перем
count_tries = 0

while is_run == True:
    count_tries += 1
    user_number  = int(input("введите число от 1 до 100 "))

    if user_number > comp_numb:
        print("введи меньше ")

    if user_number < comp_numb:
        print("введи больше")    

    if user_number == comp_numb:
        print("ура") 
        is_run= False       
print( f"вы потратили на это {count_tries} попыток")  #вставил в строку переменную