# Chapter 27: OOP - Encapsulation
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:29:56
# ============================================

# -----------------------------------------------
# SECTION 1: Basic Encapsulation
# -----------------------------------------------

print("--- Basic Encapsulation ---")


class Employee:
    """Encapsulated employee class with validation."""

    def __init__(self, name: str, salary: float, department: str):
        self.__name = name
        self.__salary = salary
        self.__department = department
        self.__performance_score = 0

    # Getters
    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def department(self) -> str:
        return self.__department

    # Setters with validation
    @salary.setter
    def salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        if new_salary < self.__salary:
            raise ValueError("Salary cannot be decreased")
        self.__salary = new_salary

    @department.setter
    def department(self, new_dept: str):
        valid_depts = ["Engineering", "Marketing", "HR", "Finance", "Sales"]
        if new_dept not in valid_depts:
            raise ValueError(f"Invalid department. Choose from {valid_depts}")
        self.__department = new_dept

    def give_raise(self, percentage: float):
        if percentage <= 0:
            raise ValueError("Raise percentage must be positive")
        self.__salary *= 1 + percentage / 100

    def __str__(self):
        return f"Employee({self.__name}, {self.__department}, ${self.__salary:,.2f})"


emp = Employee("Alice", 75000, "Engineering")
print(emp)

emp.give_raise(10)
print(f"After 10% raise: ${emp.salary:,.2f}")

emp.department = "Finance"
print(f"New dept: {emp.department}")

try:
    emp.salary = 50000  # Try to decrease salary
except ValueError as e:
    print(f"Error: {e}")

# -----------------------------------------------
# SECTION 2: Encapsulation in Data Class
# -----------------------------------------------

print("\n--- Inventory System ---")


class Inventory:
    """Encapsulated inventory management."""

    def __init__(self):
        self.__items = {}  # {item_name: quantity}
        self.__transactions = []

    def add_item(self, name: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.__items[name] = self.__items.get(name, 0) + quantity
        self.__transactions.append(f"ADD {name}: +{quantity}")

    def remove_item(self, name: str, quantity: int):
        if name not in self.__items:
            raise KeyError(f"{name} not in inventory")
        if self.__items[name] < quantity:
            raise ValueError(f"Insufficient {name}")
        self.__items[name] -= quantity
        if self.__items[name] == 0:
            del self.__items[name]
        self.__transactions.append(f"REMOVE {name}: -{quantity}")

    def get_quantity(self, name: str) -> int:
        return self.__items.get(name, 0)

    def get_all_items(self) -> dict:
        return dict(self.__items)  # Return copy, not reference

    def get_history(self) -> list:
        return list(self.__transactions)  # Return copy


inv = Inventory()
inv.add_item("Apple", 100)
inv.add_item("Banana", 50)
inv.add_item("Apple", 25)
inv.remove_item("Apple", 30)

print("Inventory:", inv.get_all_items())
print("Apple quantity:", inv.get_quantity("Apple"))
print("Transaction history:")
for tx in inv.get_history():
    print(f"  {tx}")

print("\n" + "=" * 50)
print("Chapter 27 Complete!")
print("=" * 50)
