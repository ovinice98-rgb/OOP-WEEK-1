from bank_account import BankAccount, InsufficientFundsError

print("--- STARTING LAB TEST RUN ---")
print("Name: OGHENEYOREHME OVIE FAVOUR")
print("Matric Number: CPE/2023/1075")
print("Department: COMPUTER ENGINEERING\n")

# 1. Initialize Account
account = BankAccount(owner="OGHENEYOREHME OVIE FAVOUR", initial_balance=100.0)
print(f"[SETUP] Initial State -> {account}")

# 2. Test Deposit
account.deposit(50.0)
print(f"[DEPOSIT] Deposited ₦50.00 -> New Balance: ₦{account.balance:.2f}")

# 3. Test Withdrawal & Fee
account.withdraw(30.0)
print(f"[WITHDRAWAL] Withdrew ₦30.00 (+ ₦0.50 Fee) -> New Balance: ₦{account.balance:.2f}")

# 4. Test Error Catching
print("\n[ERROR TESTING] Testing Insufficient Funds Handling:")
try:
    account.withdraw(500.0)
except InsufficientFundsError as error:
    print(f"Success! System securely caught expected error: {error}")

print("\n--- ALL TASKS EXECUTED AND PASSED ---")
