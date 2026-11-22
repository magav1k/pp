#Известны две скорости: одна в километрах в час, другая — в метрах в секунду. Какая из скоростей больше?
print("=============================")
km_in_hour = int(input("введите км в час(1 скорость): "))
meters_in_sec = int(input("введите метры в секунду(2 скорость): "))
print("")
km_in_hour = km_in_hour*1000/3600

if km_in_hour > meters_in_sec:
    print(f"1 скорость: {km_in_hour} , больше 2 : {meters_in_sec} ")
else:
    print(f"2 скорость: {meters_in_sec} , больше 2 : {km_in_hour} ")
print("=============================")