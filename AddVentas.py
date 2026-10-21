Productname = "cascaras de uvas"
Stock = 100
Price = 10.99
ProductId = "67676767"
Membership = "Manuel67"
Quantity = 67
payment = Price * Quantity

Membership = input("Enter the membership name: ")
ProductId = input("Enter the product ID: ")
Productname = input("Enter the product name: ")
Quantity = int(input("Enter the quantity: "))
Stock = int(input("Enter the stock available: "))
if Quantity > Stock:
    print("No hay suficiente stock disponible.")
print("el precio sería " + str(payment) + " pesos")
if payment >= Price * Quantity:
    print("El pago es suficiente para la compra.")