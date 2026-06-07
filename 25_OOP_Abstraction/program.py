# Chapter 25: OOP - Abstraction
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:02:05
# ============================================

from abc import ABC, abstractmethod
import math

# -----------------------------------------------
# SECTION 1: Abstract Base Class
# -----------------------------------------------

print("--- Abstract Base Class ---")

class Shape(ABC):
    """Abstract base class for all shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area. MUST be implemented."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter. MUST be implemented."""
        pass
    
    # Concrete method - already implemented in abstract class
    def describe(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")

# Cannot instantiate abstract class!
try:
    s = Shape()
except TypeError as e:
    print(f"Cannot create Shape: {e}")

# -----------------------------------------------
# SECTION 2: Concrete Implementations
# -----------------------------------------------

print("\n--- Concrete Shapes ---")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius ** 2
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class EquilateralTriangle(Shape):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.side ** 2
    def perimeter(self) -> float:
        return 3 * self.side

shapes = [Circle(5), Rectangle(4, 6), EquilateralTriangle(6)]
for shape in shapes:
    print(shape.describe())

# -----------------------------------------------
# SECTION 3: Abstract Class for Payment Gateway
# -----------------------------------------------

print("\n--- Payment Gateway (Real-world Abstraction) ---")

class PaymentGateway(ABC):
    """Abstract payment gateway - defines the interface."""
    
    @abstractmethod
    def connect(self) -> bool:
        """Establish connection to payment provider."""
        pass
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        """Process a payment and return transaction result."""
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """Refund a transaction."""
        pass
    
    def validate_amount(self, amount: float) -> bool:
        """Concrete method: validate payment amount."""
        return amount > 0

class StripeGateway(PaymentGateway):
    def connect(self) -> bool:
        print("  Connecting to Stripe...")
        return True
    def process_payment(self, amount: float, currency: str) -> dict:
        if not self.validate_amount(amount):
            return {"status": "failed", "error": "Invalid amount"}
        return {"status": "success", "id": "stripe_123", "amount": amount}
    def refund(self, transaction_id: str) -> bool:
        print(f"  Stripe refund for {transaction_id}")
        return True

class PayPalGateway(PaymentGateway):
    def connect(self) -> bool:
        print("  Connecting to PayPal...")
        return True
    def process_payment(self, amount: float, currency: str) -> dict:
        return {"status": "success", "id": "paypal_456", "amount": amount}
    def refund(self, transaction_id: str) -> bool:
        print(f"  PayPal refund for {transaction_id}")
        return True

def charge_customer(gateway: PaymentGateway, amount: float):
    """Works with ANY payment gateway - this is abstraction in action."""
    gateway.connect()
    result = gateway.process_payment(amount, "USD")
    print(f"  Payment result: {result}")

for gw in [StripeGateway(), PayPalGateway()]:
    charge_customer(gw, 99.99)

print("\n" + "="*50)
print("Chapter 25 Complete!")
print("="*50)