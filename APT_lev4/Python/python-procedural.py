# nhif_system.py

CO_PAYMENT_RATE = 0.10

def calculate_claim(amount):
    return amount - (amount * CO_PAYMENT_RATE)

def process_claim(name, policy_number, amount):
    co_payment = amount * CO_PAYMENT_RATE
    covered = calculate_claim(amount)

    print("\n=== NHIF Claim Summary ===")
    print(f"Patient     : {name}")
    print(f"Policy No.  : {policy_number}")
    print(f"Total Bill  : KES {amount:.2f}")
    print(f"Co-payment  : KES {co_payment:.2f}")
    print(f"NHIF Covers : KES {covered:.2f}")

def main():
    name = input("Enter patient name: ")
    policy_number = input("Enter policy number: ")
    amount = float(input("Enter total bill amount (KES): "))

    process_claim(name, policy_number, amount)

main()
