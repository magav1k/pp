print("=====================")
ticket = 0

left_part = 0
right_part = 0

number1 = 0
number2 = 0
number3 = 0

sum_left = 0
sum_right = 0

ticket = int(input("введите номер билета(6 цифр): "))

left_part = ticket // 1000
right_part = ticket % 1000

number1 = left_part // 100
number2 = left_part % 10
number3 = left_part // 10 % 10

sum_left = number1 + number2 +number3

number1 = right_part // 100
number2 = right_part % 10
number3 = right_part // 10 % 10

sum_right = number1 + number2 +number3
print()
if sum_left==sum_right:
    print("билет счастливый")
else:
    print("билет не счастливый")

print("=====================")
