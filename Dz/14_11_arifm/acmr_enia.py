count_panel = int(input("введите число панелей: "))
widht_panel = int(input("введите ширину панелей: "))
lengt_panel = int(input("введите длинну панелей: "))
count_sulfur = 0
COUNT_SULF_ON_QWAD_METER = 1

count_sulfur = lengt_panel * widht_panel * COUNT_SULF_ON_QWAD_METER * count_panel * 2
print()
print(f"необходимо сульфида: {count_sulfur}")