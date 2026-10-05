# Kirill Kaminskyi M7P5.py 10/5/2026

total_discount = 0
#input
do_program = input("Do you want to do this program? ")

#process
do_program = do_program.lower()

while do_program == "yes":
    item_quantity = int(input("Enter your item quantity: "))
    item_price = float(input("Enter your item price: "))

    extended_price = item_price * item_quantity

    if extended_price > 10000:
        discount_amount = extended_price * 0.25
    else :
        discount_amount = extended_price * 0.10

    total = extended_price - discount_amount

#output
    print(f"Extended price: ${extended_price:.,2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Total price: ${total:.2f}")

#process
    total_discount = total_discount + discount_amount

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()

#output
print(f"Total discount: ${total_discount:.2f}")