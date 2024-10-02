def coffee_and_muffin_receipt():
    #prices
    coffee_price = 5.00
    muffin_price = 4.00
    cookie_price = 3.00
    bagel_price = 4.00
    tax_rate = 0.06
    
    #Asks input for amount of coffees and muffins
    num_coffee = int(input('Number of coffees bought?'))
    num_muffins = int(input('Number of muffins bought?'))
    num_cookies = int(input('Number of cookies bought?'))
    num_bagels = int(input('Number of bagels bought?'))

    #subtotal and tax calculation
    coffee_subtotal = num_coffee * coffee_price
    muffin_subtotal = num_coffee * muffin_price
    cookie_subtotal = num_cookies * cookie_price
    bagel_subtotal = num_bagels * bagel_price
    subtotal = coffee_subtotal + muffin_subtotal + cookie_subtotal + bagel_subtotal
    tax = subtotal * tax_rate
    total = subtotal + tax

    #print display
    print("********************")
    print("My Coffee and Muffin Shop Receipt")
    num_coffee = int(input('Number of coffees bought?'))
    print(num_coffee)
    num_muffins = int(input('Number of muffins bought?'))
    print(num_muffins)
    num_cookies = int(input('Number of cookies bought?'))
    print(num_cookies)
    num_bagels = int(input('Number of bagels bought?'))
    print(num_bagels)
    print("********************")
    print()
    print("********************")
    print("My coffee and Muffin Shop Receipt")
    print(f"{num_coffee} Coffee at ${coffee_price} each: ${coffee_subtotal: .2f}")
    print(f"{num_muffins} Muffins at ${muffin_price} each: ${muffin_subtotal: .2f}")
    print(f"{num_cookies} Muffins at ${cookie_price} each: ${cookie_subtotal: .2f}")
    print(f"{num_bagels} Muffins at ${bagel_price} each: ${bagel_subtotal: .2f}")
    print(f"6% tax: 4{tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("********************")

if __name__ == "_main_":
    coffee_and_muffin_receipt()
