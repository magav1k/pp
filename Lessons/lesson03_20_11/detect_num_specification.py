symbol = input("введите символ: ")

if (symbol>="a" and symbol<="z") or (symbol>="A" and symbol<="Z"):
    print("это буква")

    if (symbol>="a" and symbol<="z"):
        print("маленькая")

    else: print("большая")    

elif symbol>="0" and symbol<="9":
    print("это цифра")

    if ord(symbol) % 2 == 0:# ORD превращает символ в его код, который видит компьютер, обычно четные циифры имеют четный код, они идут диапазоном, сравнивает компьютер символы по коду
        print("четная")
    else:
        print("не четная")   

elif (
    symbol >= "!"
    and symbol <= "/"
    or symbol >= ":"
    and symbol <= "@"
    or symbol >= "["
    and symbol <= "`"
    or symbol >= "{"
    and symbol <= "~" 
    ):
    print("Это спец символ")

else:
    print("это хз что такое")