actual_price=float(input("Enter the actual product price: "))
sale_amt=float(input("Enter the sale amount of product: "))
if sale_amt>actual_price:
    profit=sale_amt-actual_price
    print("Profit: ",profit)
else:
    loss=actual_price-sale_amt
    print("Loss: ",loss)