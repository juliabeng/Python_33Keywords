# Define a class for Bank Account
class BankAccount:
    interest_rate = 0.05  # Class attribute
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def transfer(self, amount, recipient):
        if self is recipient:
            return "Cannot transfer to the same account"
        try:
            self.withdraw(amount)
            recipient.deposit(amount)
        except ValueError as e:
            return f"Transfer failed: {e}"
        finally:
            pass  # Placeholder, could log transaction details
        return f"Transfer successful! {self.owner} -> {recipient.owner}: {amount}"

# Function demonstrating global and nonlocal variables
def manage_global_interest():
    global interest_rate
    interest_rate = 0.06  # Modify global variable
    
    interest = 0.05  # Local variable
    
    def inner_function():
        nonlocal interest
        interest = 0.07  # Modify nonlocal variable
        return interest
    
    return inner_function()

def example_lambda():
    return lambda x: x * 2  # Lambda function demonstration

# Main execution
def main():
    accounts = [
        BankAccount("Alice", 1000),
        BankAccount("Bob", 500)
    ]
    
    for acc in accounts:
        print(f"{acc.owner} has balance: {acc.balance}")
    
    print(accounts[0].transfer(200, accounts[1]))
    
    # Demonstrating try-except-finally
    try:
        accounts[1].withdraw(1000)
    except ValueError as e:
        print("Exception caught:", e)
    finally:
        print("End of withdrawal attempt")
    
    # Demonstrating while loop with break and continue
    num_attempts = 0
    while True:
        num_attempts += 1
        if num_attempts % 2 == 0:
            continue  # Skip even attempts
        if num_attempts > 5:
            break  # Exit loop after 5 attempts
        print("Attempt", num_attempts)
    
    # Using "is" and "in" keywords
    acc1 = accounts[0]
    acc2 = accounts[1]
    print("Same account?", acc1 is acc2)
    print("Alice's account in list?", acc1 in accounts)
    
    # Using None and del
    temp = None
    print("Temporary value:", temp)
    del temp  # Delete variable
    
    # Demonstrating yield
    def generate_numbers():
        for i in range(3):
            yield i
    
    for num in generate_numbers():
        print("Generated number:", num)
    
    # Example use of True and False
    print("True or False?", True or False)
    print("True and False?", True and False)
    print("Not True?", not True)
    
    # Demonstrating nonlocal usage
    print("Updated interest rate from inner function:", manage_global_interest())

# Run main program
if __name__ == "__main__":
    main()
