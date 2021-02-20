from bill import split_bill

items = [
    {"name": "Arroz", "price": 305, "quantity": 1},
    {"name": "Carne", "price": 20, "quantity": 0},
]
emails = [
    "person1@example.com",
    "person2@example.com",
    "person3@example.com",
]

print(split_bill(items, emails))
