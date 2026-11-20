after_num=int(input("введи число которое получилось: "))
before_num = 0
before_num = after_num //100 + (after_num % 100) * 10
print(f"число было: {before_num}")