year = int(input())
day =0
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    day = 256-244
else: day = 256-243
print(f"{day:02}/09/{year:04d}")
