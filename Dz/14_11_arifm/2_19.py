print("=====================")
num = 0

left_part = 0
right_part = 0

number1 = 0
number2 = 0

sum = 0
multi = 0

num = int(input("введите число(4 цифры): "))

left_part = num // 100
right_part = num % 100

number1 = left_part // 10
number2 = left_part % 10

sum = number1 + number2
multi = number1 * number2

number1 = right_part // 10
number2 = right_part % 10

sum = sum + number1 + number2
multi = multi * number1 * number2
print()

print(f"сумма цифр: {sum}")
print(f"произведение цифр: {multi}")

print("=====================")