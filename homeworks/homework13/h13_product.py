# «Товар и корзина». Класс Product (title, price, quantity) с методом total_price() (цена × количество).
# Класс Cart, который хранит список продуктов и методы add(product), total_sum() и show().
# Добавить несколько товаров, вывести общую сумму.


class Product:
    def __init__(self, title: str, price: float, quantity: int) -> None:
        self.title = title
        self.price = price
        self.quantity = quantity
        
    def total_price(self) -> float:
        return self.price * self.quantity
    
    
class Cart:
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def total_sum(self) -> float:
        return sum(product.total_price() for product in self.products)

    def show(self) -> None:
        for product in self.products:
            print(
                f"{product.title}: {product.price} руб. x "
                f"{product.quantity} шт. = {product.total_price()} руб."
            )


if __name__ == "__main__":
    laptop = Product(title="Ноутбук", price=100000, quantity=10)
    smartphone = Product(title="Смартфон", price=20000, quantity=15)
    television = Product(title="Телевизор", price=150000, quantity=4)
    tablet = Product(title="Планшет", price=15000, quantity=40)

    cart = Cart()
    
    cart.add(laptop)
    cart.add(smartphone)
    cart.add(television)
    cart.add(tablet)

    cart.show()

    print(f"Общая сумма товаров: {cart.total_sum()}")
