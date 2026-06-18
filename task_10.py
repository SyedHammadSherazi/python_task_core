# Build a shopping cart that supports adding and removing items (using a list).
add_product=["shoes", "toy", "orange", "banana"]
add_product_by=add_product.append((input("enter the product name : ")))
print("product name is : ",add_product) 
add_product.remove(input("remove the product from cart :" ))
print("product is remove from the cart :" , add_product)

