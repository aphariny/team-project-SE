"""Product catalogue module for the team shopping project."""

PRODUCTS = [
    {"id": 1, "name": "Notebook", "price": 50.00},
    {"id": 2, "name": "Pen", "price": 10.00},
    {"id": 3, "name": "Backpack", "price": 650.00},
]

def list_products():
    """Display all available products."""
    for product in PRODUCTS:
        print(
            f'{product["id"]}. {product["name"]} - '
            f'Rs. {product["price"]:.2f}'
        )


if __name__ == "__main__":
    list_products()
