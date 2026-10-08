from eshop_manager.models import InvalidProductDataError, Product
from eshop_manager.services import (
    calculate_inventory_value,
    filter_by_category,
    find_most_expensive_product,
    find_product_by_name,
)


def create_demo_products() -> list[Product]:
    """Створення початкових демонстраційних даних."""
    return [
        Product(name="Ноутбук Lenovo", category="Електроніка", price=28500.0, quantity=5),
        Product(name="Смартфон Samsung", category="Електроніка", price=19999.0, quantity=8),
        Product(name="Кавоварка Philips", category="Побутова техніка", price=6400.0, quantity=3),
        Product(name="Мишка бездротова", category="Аксесуари", price=850.0, quantity=15),
    ]


def print_products(products: list[Product]) -> None:
    """Форматоване виведення списку товарів."""
    if not products:
        print("\nСписок товарів порожній.")
        return

    print("\n" + "=" * 65)
    print(f"{'Назва':25} | {'Категорія':18} | {'Ціна (грн)':10} | {'К-сть':5}")
    print("-" * 65)
    for p in products:
        print(f"{p.name:25} | {p.category:18} | {p.price:10.2f} | {p.quantity:5d}")
    print("=" * 65)


def add_product_cli(products: list[Product]) -> None:
    """Додавання товару через консоль із валідацією."""
    name = input("Введіть назву товару: ").strip()
    if not name:
        print("Помилка: назва не може бути порожньою.")
        return

    category = input("Введіть категорію: ").strip()
    if not category:
        print("Помилка: категорія не може бути порожньою.")
        return

    try:
        price = float(input("Введіть ціну: "))
        quantity = int(input("Введіть кількість: "))
        new_product = Product(name=name, category=category, price=price, quantity=quantity)
        products.append(new_product)
        print(f"Товар '{name}' успішно додано!")
    except ValueError:
        print("Помилка: ціна та кількість мають бути числовими значеннями.")
    except InvalidProductDataError as err:
        print(f"Помилка створення товару: {err}")


def print_menu() -> None:
    print("\n--- Меню Інтернет-Магазину ---")
    print("1. Показати всі товари")
    print("2. Додати новий товар")
    print("3. Обчислити загальну вартість залишків")
    print("4. Знайти товар за назвою")
    print("5. Фільтрувати за категорією")
    print("6. Показати найдорожчий товар")
    print("0. Вихід")


def main() -> None:
    products = create_demo_products()

    while True:
        print_menu()
        choice = input("Оберіть дію (0-6): ").strip()

        if choice == "1":
            print_products(products)
        elif choice == "2":
            add_product_cli(products)
        elif choice == "3":
            total_val = calculate_inventory_value(products)
            print(f"\nЗагальна вартість усіх залишків на складі: {total_val:.2f} грн")
        elif choice == "4":
            name = input("Введіть назву для пошуку: ")
            product = find_product_by_name(products, name)
            if product:
                print(f"Знайдено: {product.name} ({product.category}) — {product.price:.2f} грн, {product.quantity} шт.")
            else:
                print("Товар з такою назвою не знайдено.")
        elif choice == "5":
            cat = input("Введіть назву категорії: ")
            filtered = filter_by_category(products, cat)
            print_products(filtered)
        elif choice == "6":
            expensive = find_most_expensive_product(products)
            if expensive:
                print(f"Найдорожчий товар: {expensive.name} — {expensive.price:.2f} грн")
            else:
                print("Список товарів порожній.")
        elif choice == "0":
            print("Роботу завершено. До побачення!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()