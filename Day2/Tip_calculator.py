print("Welcome to Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to add 11,20,30 ?"))
split=int(input("How many people to split the bill ?"))
bill_with_tip= tip/100 * bill+bill
bill_per_person=bill_with_tip/split
final_amount=round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")