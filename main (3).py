
class BankAccount:
  """A class to represent a bank account."""

  def __init__(self, account_number, balance):
    """Initializes a new bank account.

    Args:
      account_number: The account number.
      balance: The initial balance.
    """
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):
    """Deposits money into the account.

    Args:
      amount: The amount to deposit.
    """
    self.balance += amount

  def withdraw(self, amount):
    """Withdraws money from the account.

    Args:
      amount: The amount to withdraw.
    """
    self.balance -= amount

  def get_balance(self):
    """Returns the current balance of the account."""
    return self.balance

# Example usage:

account = BankAccount(1234567890, 100)

# Deposit $50
account.deposit(50)

# Withdraw $25
account.withdraw(25)

# Get the current balance
balance = account.get_balance()

print("The current balance is: {}".format(balance))
