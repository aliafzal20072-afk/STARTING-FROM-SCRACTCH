Days = int(input("enter number of days:"))

expense = []

for i in range(1, Days + 1):
    amount = int(input(f"enter expense for day {1}:"))
    expense.append(amount)

total = sum(expense)   
average = total/Days

print("\nExpense: ", expense)
print("Total amount: ", total)
print("Average amount: ", average)