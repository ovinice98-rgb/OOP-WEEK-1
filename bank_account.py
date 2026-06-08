class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    # Class attribute for the transaction fee (50 kobo / ₦0.50)
    transaction_fee = 0.50

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._owner = owner
        self._balance = float(initial_balance)

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def owner(self) -> str:
        return self._owner

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        total_deduction = amount + BankAccount.transaction_fee
        
        if total_deduction > self._balance:
            raise InsufficientFundsError(
                f"Insufficient funds! You need ₦{total_deduction:.2f} "
                f"but only have ₦{self._balance:.2f}."
            )
        
        self._balance -= total_deduction

    @classmethod
    def from_dict(cls, data: dict):
        return cls(owner=data['owner'], initial_balance=data.get('balance', 0.0))

    def __str__(self) -> str:
        return f"BankAccount Owner: {self._owner}, Balance: ₦{self._balance:.2f}"
