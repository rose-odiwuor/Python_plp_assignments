def calculate_discount(price, discount_percent):

    # Check if the discount percentage is 20% or higher

    if discount_percent >= 20:

        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price

        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    
    else:
        # Return the original price if the discount is less than 20%
        return price
    
# Prompt user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Check if the discount was applied
if final_price == price:
    print(f"No discount applied. The original price is: {final_price:.2f}")
else:
    print(f"The final price after applying the discount is: {final_price:.2f}")