bank_larri_true = int(input("сколько банок сбил ларри(max 10): "))
bank_garri_true = int(input("сколько банок сбил гарри(max 10): "))
if bank_larri_true <= 10 and bank_garri_true <=10:
    print(f"ларри не сбил: {bank_garri_true-1} банок\nгарри не сбил {bank_larri_true-1} банок")
else: 
    print("максимум 10 банок!")