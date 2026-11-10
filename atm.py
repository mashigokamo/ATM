PIN = "1234"
INITIAL_BALANCE = 1000.00
MAX_PIN_ATTEMPTS = 3


def authenticate():
    for attempt in range(MAX_PIN_ATTEMPTS):
        entered_pin = input("Enter your PIN: ").strip()
        if entered_pin == PIN:
            print("PIN accepted. Welcome!\n")
            return True

        remaining_attempts = MAX_PIN_ATTEMPTS - attempt - 1
        if remaining_attempts:
            print(f"Incorrect PIN. {remaining_attempts} attempt(s) remaining.")
        else:
            print("Incorrect PIN. Your account is locked.")

    return False


def read_amount(prompt):
    try:
        amount = float(input(prompt).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

    if amount <= 0:
        print("Amount must be greater than zero.")
        return None

    return amount


def run_atm():
    balance = INITIAL_BALANCE
    if not authenticate():
        return

    while True:
        print("ATM Menu")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw cash")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            print(f"Your balance is ${balance:.2f}\n")
        elif choice == "2":
            amount = read_amount("Enter deposit amount: $")
            if amount is not None:
                balance += amount
                print(f"Deposit successful. New balance: ${balance:.2f}\n")
        elif choice == "3":
            amount = read_amount("Enter withdrawal amount: $")
            if amount is not None:
                if amount > balance:
                    print("Insufficient funds.\n")
                else:
                    balance -= amount
                    print(f"Please take your cash. New balance: ${balance:.2f}\n")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    run_atm()