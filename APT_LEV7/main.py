import re

# Sample balances
accounts = {
    "A": 6000,
    "B": 2000
}

def parse_command(command):
    pattern = r"TRANSFER (\d+) FROM (\w+) TO (\w+) IF BALANCE > (\d+)"
    match = re.match(pattern, command)

    if not match:
        raise ValueError("Invalid command format")

    amount = int(match.group(1))
    sender = match.group(2)
    receiver = match.group(3)
    condition_balance = int(match.group(4))

    return amount, sender, receiver, condition_balance


def interpret(command):
    try:
        amount, sender, receiver, condition_balance = parse_command(command)

        print(f"Parsed → Amount: {amount}, From: {sender}, To: {receiver},  Balance > {condition_balance}")

        # Check if sender exists
        if sender not in accounts or receiver not in accounts:
            print("❌ Invalid accounts")
            return

        # Validate condition
        if accounts[sender] > condition_balance:
            if accounts[sender] >= amount:
                # Perform transfer
                accounts[sender] -= amount
                accounts[receiver] += amount

                print("✅ Transaction successful")
            else:
                print("❌ Insufficient funds")
        else:
            print("❌ not met (balance too low)")

    except Exception as e:
        print(f"Error: {e}")


# Test
print("Format: TRANSFER <amount> FROM <sender> TO <receiver> IF BALANCE > <value>")
command = input("Enter Command: ")
interpret(command)

print("\nUpdated balances:", accounts)
