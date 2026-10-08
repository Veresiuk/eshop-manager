from dataclasses import dataclass


class InvalidProductDataError(Exception):
    """Виняток для некоректних даних товару."""
    pass


@dataclass
class Product:
    """Модель товару інтернет-магазину."""
    name: str
    category: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise InvalidProductDataError("Ціна не може бути від'ємною.")
        if self.quantity < 0:
            raise InvalidProductDataError("Кількість не може бути від'ємною.")

    @property
    def total_cost(self) -> float:
        """Вартість залишку поточного товару на складі."""
        return self.price * self.quantity