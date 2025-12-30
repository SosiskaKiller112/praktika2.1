def calc_salary():
    print("=" * 40)
    print("Расчет заработной платы")
    print("=" * 40)
    
    try:
        hours_worked = float(input("Отработано часов: "))
        hourly_rate = float(input("Ставка в час (руб): "))
        
        if hours_worked <= 0 or hourly_rate <= 0:
            print("Ошибка: значения должны быть положительными")
            return
        
        total = hours_worked * hourly_rate
        
        print("\n" + "-" * 40)
        print("РЕЗУЛЬТАТ РАСЧЕТА")
        print("-" * 40)
        print(f"Часы: {hours_worked}")
        print(f"Ставка: {hourly_rate:.2f} руб/час")
        print(f"К выплате: {total:.2f} руб")
        print("-" * 40)
        
    except:
        print("Ошибка ввода данных")

def batch_calc():
    print("=" * 40)
    print("Групповой расчет зарплат")
    print("=" * 40)
    
    records = []
    
    while True:
        print(f"\nЗапись #{len(records)+1}")
        fio = input("Фамилия И.О. (пусто - закончить): ")
        if not fio.strip():
            break
            
        try:
            h = float(input("Часы работы: "))
            r = float(input("Ставка: "))
            
            if h <= 0 or r <= 0:
                print("Некорректные значения, пропускаем...")
                continue
                
            pay = h * r
            records.append((fio, h, r, pay))
            
        except:
            print("Ошибка ввода, попробуйте снова")
    
    if records:
        print("\n" + "=" * 60)
        print("СВОДНЫЙ ОТЧЕТ")
        print("=" * 60)
        print(f"{'№':<4}{'Сотрудник':<20}{'Часы':<8}{'Ставка':<10}{'Сумма':<12}")
        print("-" * 60)
        
        total_all = 0
        for idx, (name, hrs, rt, amt) in enumerate(records, 1):
            print(f"{idx:<4}{name:<20}{hrs:<8.1f}{rt:<10.2f}{amt:<12.2f}")
            total_all += amt
        
        print("-" * 60)
        print(f"{'ИТОГО:':<34}{total_all:<12.2f}")
        print("=" * 60)

def run():
    while True:
        print("\n" + "=" * 30)
        print("КАЛЬКУЛЯТОР ЗАРПЛАТ")
        print("=" * 30)
        print("1 - Один сотрудник")
        print("2 - Несколько сотрудников")
        print("3 - Завершить работу")
        
        opt = input("Ваш выбор: ")
        
        if opt == "1":
            calc_salary()
        elif opt == "2":
            batch_calc()
        elif opt == "3":
            print("Работа завершена")
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    run()
