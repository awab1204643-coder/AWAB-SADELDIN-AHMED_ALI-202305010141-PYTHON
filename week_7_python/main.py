from food_order import calculate_total


def main():
    try:
        price = float(input("Price (RM): "))
    except ValueError:
        print("invalid price")
        return

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("invalid quantity")
        return

    total = calculate_total(price, quantity)
    if isinstance(total, str):
        print(total)
    else:
        print(f"Total Payment = RM {total:.2f}")


if __name__ == "__main__":
    main()
