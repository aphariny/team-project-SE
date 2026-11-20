"""Shopping cart module for the team shopping project."""

def add_to_cart(cart, product, quantity=1):
    """Add a product and quantity to the cart."""
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    for item in cart:
        if item["product"]["id"] == product["id"]:
            item["quantity"] += quantity
            return cart

    cart.append({"product": product, "quantity": quantity})
    return cart


def display_cart(cart):
    """Display cart items and the total amount."""
    total = 0
    for item in cart:
        product = item["product"]
        subtotal = product["price"] * item["quantity"]
        total += subtotal
        print(f'{product["name"]} x {item["quantity"]} = Rs. {subtotal:.2f}')
    print(f"Total: Rs. {total:.2f}")


if __name__ == "__main__":
    sample_cart = []
    add_to_cart(sample_cart, {"id": 1, "name": "Notebook", "price": 50.0}, 2)
    add_to_cart(sample_cart, {"id": 2, "name": "Pen", "price": 10.0})
    display_cart(sample_cart)
    def remove_from_cart(cart, product_id):
    """Remove a product from the cart."""
    return [
        item for item in cart
        if item["product"]["id"] != product_id
    ]
