count_cube = 0
count_cube_lenght = 0 
count_cube_wight = 0
print("===================")
lengh_pr = int(input("введите длинну прямоугольника из которог вырезаете: "))

wight_pr =int(input("введите ширину прямоугольника из которог вырезаете: "))

poligon_qwad = int(input("введите длину квадратика который вырезаете: "))

#сколько влазит в длинну целиком
count_cube_lenght = lengh_pr // poligon_qwad
#скока в шиирну
count_cube_wight = wight_pr // poligon_qwad

count_cube = count_cube_lenght * count_cube_wight
print()
print(f"из прямоугольника можно вырезать: {count_cube} квадратиков")
print("===================")