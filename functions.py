def calculate_discount(price,discount_percent):

    

    if discount_percent  >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    

original = float(input("enter the original price:"))
discount = float(input("enter the discount percentage:"))
    
final_price = calculate_discount(original,discount)
print(f"The final price is: {final_price}")
