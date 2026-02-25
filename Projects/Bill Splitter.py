print("Welcome to Bill Splitter")
Bill = float(input("ENTER YOUR TOTAL BILL: $"))
Tip = int(input("How much Tip would you like to pay (10%, 12%, 15%) :" ))
Number_ppl = int(input("How many people would you like to split the bill with: "))

tip_as_percentage = Tip / 100
total_tip = Bill * tip_as_percentage
total_bill = Bill + total_tip
bill_ppl = total_bill / Number_ppl
final_bill = round(bill_ppl, 2)

print(f"Each person should pay ${final_bill}")