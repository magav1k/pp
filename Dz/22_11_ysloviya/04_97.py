num1=int(input("введите 1 число: "))
num2=int(input("введите 2 число: "))
num3=int(input("введите 3 число: "))
big_num =0
litl_num =0
medium_num=0
if num1>num2 and num1>num3:
    big_num=num1
    if num2>num3:
        litl_num =num3
        medium_num=num2
    elif num2<num3:
        litl_num =num2
        medium_num=num3
        
if num2>num1 and num2>num3:
    big_num=num2
    if num1>num3:
        litl_num =num3
        medium_num=num1
    elif num1<num3:
        litl_num =num1
        medium_num=num3    

if num3>num2 and num3>num1:
    big_num=num3
    if num2>num1:
        litl_num =num1
        medium_num=num2
    elif num2<num1:
        litl_num =num2
        medium_num=num1
print(f"самое большое: {big_num} самое маленькое: {litl_num} среднее: {medium_num}")