def calculate_total(price, quantity):
    # Validate price
    if not isinstance(price, (int, float)):
        return "invalid price"
    if price <= 0:
        return "invalid price"

    # Validate quantity
    if not isinstance(quantity, int):
        return "invalid quantity"
    if quantity <= 0:
        return "invalid quantity"

    return price * quantity
