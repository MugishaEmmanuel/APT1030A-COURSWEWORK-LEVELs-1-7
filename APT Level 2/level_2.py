name = input("Enter your Name: ")
mem_id = int(input("Enter your Member ID: "))
total_saving = 0

for i in range(1,7):
    monthly_cont = int(input(f"Enter month {i} contribution: "))
    total_saving += monthly_cont

print(f"Hello,{name}\nMember ID:{mem_id}")
print(f"Total Savings last 6 months: {total_saving} KES")