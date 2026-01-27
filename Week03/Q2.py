#Question 2: Shopping cart (lists - searching and removal)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs",]
apple_count = cart.count("apple")
print("there are",apple_count, "apples.")
print("milk position:", cart.index("milk"))
cart.remove("apple")
print("remove item using pop", cart.pop())
print("is banana in the cart?", "banana" in cart)
print("final cart:", cart)