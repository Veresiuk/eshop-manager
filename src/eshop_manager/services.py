from eshop_manager.models import Product


def calculate_inventory_value(products: list[Product]) -> float:
    """Обчислення загальної вартості всіх залишків товарів."""
    return sum(product.total_cost for product in products)


def find_product_by_name(products: list[Product], name: str) -> Product | None:
    """Пошук товару за назвою (без урахування регістру)."""
    search_name = name.strip().lower()
    for product in products:
        if product.name.lower() == search_name:
            return product
    return None


def filter_by_category(products: list[Product], category: str) -> list[Product]:
    """Фільтрація списку товарів за категорією."""
    filter_category = category.strip().lower()
    return [
        product
        for product in products
        if product.category.lower() == filter_category
    ]


def find_most_expensive_product(products: list[Product]) -> Product | None:
    """Визначення найдорожчого товару за одиницю вартості."""
    if not products:
        return None
    return max(products, key=lambda product: product.price)