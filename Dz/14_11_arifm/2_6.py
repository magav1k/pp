dano_sec=0
final_hour=0
final_min=0
final_sec=0


print("====================")

dano_sec=int(input("напиши секунды прошедшие с начала дня и я скажу тебе время: "))

final_hour = dano_sec // 3600
final_min = dano_sec % 3600 //60
final_sec = dano_sec % 3600 % 60 

print()
print(f"время:\n часов: {final_hour}\n минут: {final_min}\nсекунд: {final_sec}")

print("====================")