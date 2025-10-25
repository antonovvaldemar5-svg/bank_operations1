# Главный модуль программы
from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """Демонстрирует функциональность маскрировки"""
    print("БАНКОВСКАЯ МАСКА")
    # Пример с картой
    card = 1234567890123456
    masked_card = get_mask_card_number(card)
    print(f"Карта: {masked_card}")

    # Пример со счетом

    account = 1234567890
    masked_account = get_mask_account((account))
    print(f"Счет: {masked_account}")


if __name__ == "__main__":
    main()
