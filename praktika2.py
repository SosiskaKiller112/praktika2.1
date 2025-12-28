def main():
    print("=== КАЛЬКУЛЯТОР ЗАРПЛАТЫ ===")
    
    while True:
        print("\n1. Расчет зарплаты")
        print("2. Выход")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            try:
                name = input("ФИО сотрудника: ")
                hours = float(input("Отработано часов: "))
                rate = float(input("Ставка за час: "))
                
                salary = hours * rate
                
                print(f"\nРезультат для {name}:")
                print(f"Зарплата: {salary:.2f} руб.")
                
            except:
                print("Ошибка ввода данных!")
                
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

main()