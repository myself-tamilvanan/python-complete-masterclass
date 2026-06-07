# Chapter 26: OOP - Access Specifiers
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:12:48
# ============================================

# -----------------------------------------------
# SECTION 1: Public Attributes
# -----------------------------------------------

print("--- Public (name) ---")

class Person:
    def __init__(self, name, age):
        self.name = name   # Public - accessible anywhere
        self.age = age     # Public

p = Person("Alice", 30)
print(p.name)    # Accessible
print(p.age)     # Accessible
p.name = "Bob"   # Modifiable
print(p.name)

# -----------------------------------------------
# SECTION 2: Protected Attributes (_name)
# -----------------------------------------------

print("\n--- Protected (_name) ---")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._balance = balance       # Protected (convention)
        self._transaction_history = []
    
    def deposit(self, amount):
        self._balance += amount
        self._transaction_history.append(f"+{amount}")
    
    def get_balance(self):
        return self._balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# Can still access but convention says "don't"
print("Direct access (not recommended):", acc._balance)

# Subclass can access protected
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

savings = SavingsAccount("Bob", 5000, 0.05)
interest = savings.apply_interest()
print(f"Interest earned: {interest}, New balance: {savings.get_balance()}")

# -----------------------------------------------
# SECTION 3: Private Attributes (__name)
# -----------------------------------------------

print("\n--- Private (__name) ---")

class SecureBankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance    # Private - name mangled
        self.__pin = pin            # Private
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return amount
    
    def get_balance(self, pin):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")
        return self.__balance

secure_acc = SecureBankAccount("Charlie", 2000, "1234")

try:
    print("Balance:", secure_acc.get_balance("1234"))
    secure_acc.withdraw(500, "1234")
    print("After withdrawal:", secure_acc.get_balance("1234"))
except ValueError as e:
    print(f"Error: {e}")

# Name mangling: __balance becomes _SecureBankAccount__balance
print("Name mangling:", secure_acc._SecureBankAccount__balance)

# -----------------------------------------------
# SECTION 4: @property - Controlled Access
# -----------------------------------------------

print("\n--- @property ---")

class Temperature:
    """Temperature with Celsius/Fahrenheit conversion."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property - no setter needed."""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

temp.celsius = 100
print(f"Boiling: {temp.celsius}C = {temp.fahrenheit}F")

try:
    temp.celsius = -300  # Below absolute zero
except ValueError as e:
    print(f"Validation error: {e}")

print("\n" + "="*50)
print("Chapter 26 Complete!")
print("="*50)