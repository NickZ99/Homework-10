from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]


cheap_products = list(filter(lambda product: product["price"] < 100, products))
for product in cheap_products:
    print (f"- {product["name"]}: {product["price"]}")

product_info = list(map(lambda product:(product["name"], product["price"]), products))
print ("\nProducts Name and Price: ")
for name, price in product_info:
    print(f"- {name}: {price}")

sorted_products = sorted(products, key=lambda product: product["price"])
print ("\nProducts sorted by price: ")
for product in sorted_products:
    print(f"- {product["name"]}: {product["price"]}")

total_price = reduce(lambda acc, product: acc + product["price"], products, 0)
print (f"\nAll product total price: {total_price}")
