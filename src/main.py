from src.external_api import convert_to_rubles
from src.file_reader import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import search_by_description
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

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
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Статус: ").strip().upper()

        if state in ['EXECUTED', 'CANCELED', 'PENDING']:
            trans = filter_by_state(trans, state)
            print(f'Операции отфильтрованы по статусу "{state}"')
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    # Сортировка
    sort_q = input("\nОтсортировать операции по дате? Да/Нет: ").lower()
    if sort_q in ['да', 'yes', 'y', 'д']:
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        reverse = order in ['убывание', 'desc', 'd', 'у']
        trans = sort_by_date(trans, reverse=reverse)

    # Поиск по описанию
    search_q = input("\nОтфильтровать список транзакций по определенному слову "
                     "в описании? Да/Нет: ").lower()
    if search_q in ['да', 'yes', 'y', 'д']:
        word = input("Введите слово для поиска: ").strip()
        trans = search_by_description(trans, word)

    # Вывод
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans)}\n")

    if trans:
        for t in trans[:5]:
            date = get_date(t.get('date', ''))
            desc = t.get('description', '')
            from_acc = t.get('from', '')
            to_acc = t.get('to', '')

            op_amount = t.get('operationAmount', {})
            amount = op_amount.get('amount', '0')
            currency_info = op_amount.get('currency', {})
            currency = currency_info.get('code', 'RUB')

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
        print("Не найдено ни одной транзакции, подходящей под ваши "
              "условия фильтрации")


if __name__ == "__main__":
    main()
