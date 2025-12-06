from src.utils import read_json_file
from src.file_reader import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.external_api import convert_to_rubles
from src.search import search_by_description
from src.widget import mask_account_card, get_date


def main():
    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите пункт меню:")
    print("1. Транзакции из JSON-файла")
    print("2. Транзакции из CSV-файла")
    print("3. Транзакции из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    if choice == '1':
        trans = read_json_file('data/operations.json')
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        trans = read_csv_file('data/transactions.csv')
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        trans = read_excel_file('data/transactions_excel.xlsx')
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу
    while True:
        print("\nВведите статус для фильтрации.")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")
        state = input("Статус: ").strip().upper()

        if state in ['EXECUTED', 'CANCELED', 'PENDING']:
            trans = filter_by_state(trans, state)
            print(f"Отфильтровано по статусу '{state}'")
            break
        else:
            print(f"Статус '{state}' недоступен.")

    # Сортировка
    sort_q = input("\nОтсортировать по дате? (Да/Нет): ").lower()
    if sort_q in ['да', 'yes', 'y', 'д']:
        order = input("По возрастанию или убыванию? ").lower()
        reverse = order in ['убывание', 'desc', 'd', 'у']
        trans = sort_by_date(trans, reverse=reverse)

    # Только рубли
    rub_q = input("\nТолько рублевые транзакции? (Да/Нет): ").lower()
    if rub_q in ['да', 'yes', 'y', 'д']:
        trans = [t for t in trans if t.get('operationAmount', {})
        .get('currency', {}).get('code') == 'RUB']

    # Поиск по описанию
    search_q = input("\nФильтровать по слову в описании? ").lower()
    if search_q in ['да', 'yes', 'y', 'д']:
        word = input("Введите слово для поиска: ").strip()
        trans = search_by_description(trans, word)

    # Вывод
    print("\nРаспечатываю итоговый список...")
    print(f"Всего операций в выборке: {len(trans)}\n")

    if trans:
        for t in trans[:5]:
            date = get_date(t.get('date', ''))
            desc = t.get('description', '')
            from_acc = t.get('from', '')
            to_acc = t.get('to', '')
            amount = t.get('operationAmount', {}).get('amount', '0')
            currency = t.get('operationAmount', {})
            .get('currency', {}).get('code', 'RUB')

        print(f"{date} {desc}")
        if from_acc:
            print(f"{mask_account_card(from_acc)} -> ", end='')
        print(mask_account_card(to_acc))

        if currency != 'RUB':
            rub = convert_to_rubles(t)
            print(f"Сумма: {amount} {currency} (~{rub:.2f} руб.)")
        else:
            print(f"Сумма: {amount} руб.")
        print()

else:
print("Нет транзакций под ваши условия фильтрации")

if __name__ == "__main__":
    main()
