account_balance = 1000

while True:
    print(f"Account balance: ${account_balance}")
    withdrawal_amount = int(input("Amount to withdraw: "))

    if account_balance == 0:
        print("You can't withdraw")
        break
    elif withdrawal_amount <= account_balance:
        account_balance -= withdrawal_amount
        print(
            f"${withdrawal_amount} has been removed; account balance: ${account_balance}")
        continue_ = input("Do you want to withdraw again? (y/n): ")

        if continue_ == "n":
            break
        elif continue_ == "y":
            continue
        else:
            print("Invalid input")
            break
    else:
        print("Insufficient funds. Please try again")
        continue
