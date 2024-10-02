def coffee_and_muffin_receipt():
    #prices
    coffee_price = 5.00
    muffin_price = 4.00
    tax_rate = 0.06
    
    #Asks input for amount of coffees and muffins
    num_coffee = int(input('Number of coffees bought?'))
    num_muffins = int(input('Number of muffins bought?'))

    #subtotal and tax calculation
    coffee_subtotal = num_coffee * coffee_price
    muffin_subtotal = num_coffee * muffin_price
    subtotal = coffee_subtotal + muffin_subtotal
    tax = subtotal * tax_rate
    total = subtotal + tax

    #print display
    print("********************")
    print("My Coffee and Muffin Shop Receipt")
    num_coffee = int(input('Number of coffees bought?'))
    print(num_coffee)
    num_muffin = int(input('Number of muffins bought?'))
    print(num_muffin)
    print("********************")
    print()
    print("********************")
    print("My coffee and Muffin Shop Receipt")
    print(f"{num_coffee} Coffee at ${coffee_price} each: ${coffee_subtotal: .2f}")
    print(f"{num_muffin} Muffins at ${muffin_price} each: ${muffin_subtotal: .2f}")
    print(f"6% tax: 4{tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("********************")

if __name__ == "_main_":
    coffee_and_muffin_receipt()
