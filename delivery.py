"""HW1: a Bangkok food-delivery order. Practises Sessions 1-3: aliasing and defaults, comprehensions,
classes with a guarded property, __repr__ and __eq__, inheritance with super(), composition and duck typing."""


class MenuItem:
    def __init__(self, name, price):
        self.name=name
        self.price=price


    def __init__(self, name: str, price: int):
        self.name=name
        self.price=price

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        if value <= 0:
            raise ValueError("price must be more than 0")
        self._price = value

    def __repr__(self) -> str:
        return f"MenuItem('{self.name}', {self.price})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MenuItem):
            return NotImplemented
        if self.name == other.name and self.price == other.price:
            return True
        return False

    def cost(self, quantity: int) -> int:
        return self.price*quantity


class PromoItem(MenuItem):
    def cost(self, quantity):
        free=quantity//3
        paid=quantity-free
        return super().cost(paid)

    def cost(self, quantity: int) -> int:
        """Return what quantity costs when every third one is free."""
        raise NotImplementedError("core: work out the free ones, then ask super() for the cost")


class Order:
    free_delivery_from = 300

    delivery_fee = 30  # Provided: baht added to every order with food in it
    free_delivery_from = 300  # Provided: food worth this much or more is delivered free

    def __init__(self, customer: str, lines: list[tuple[MenuItem, int]] | None = None):
        self.customer=customer
        self.lines=[]
        if lines is None:
            for line in lines:
                self.lines.append(line)

    def add(self, item: MenuItem, quantity: int = 1) -> None:
        if quantity<1:
            raise ValueError("quantity must be at least 1")
        self.lines.append((item, quantity))

    def total(self) -> int:
        if len(self.lines)==0:
            return 0
        food=0
        for item, quantity in self.lines:
            food=food+item.cost(quantity)
        if food>=self.free_delivery_from:
            return food
        return food+20

    def summary(self) -> list[str]:
        result = []
        for item, quantity in self.lines:
            result.append(f"{quantity} x {item.name}")
        return result


def cheapest(options: list) -> object | None:
if len(options) == 0:
        return None
    best = options[0]
    for option in options:
        if option.total() < best.total():
            best = option
    return best

if __name__=="__main__":
    tea = PromoItem("Thai Tea", 40)
    print(tea.cost(2))
    print(tea.cost(3))
    print(tea.cost(6))
    order=Order("A")
    order.add(MenuItem("Pad Thai", 60), 2)
    print(order.total())
