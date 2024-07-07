print("welcome to the tip caluclator")
bill=float(input("how much the bill"))
tip = int(input("how much tip you can give 10,15"))
people = int(input("how many members you want to share the people"))
tip_as_percentage = tip/100
total_bill = bill + tip_as_percentage
total_amount_share = total_bill /people
final_amount =round(total_amount_share,2)
print(f"each person should pay${final_amount}")
