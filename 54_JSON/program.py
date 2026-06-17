# Chapter 54: JSON
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import json
import os

# -----------------------------------------------
# SECTION 1: json.dumps() - Python to JSON string
# -----------------------------------------------

print("--- json.dumps() ---")

person = {"name": "John", "age": 30, "city": "New York", "active": True, "score": None}

# Convert to JSON string
json_str = json.dumps(person)
print("JSON string:", json_str)
print("Type:", type(json_str))

# Pretty print with indentation
json_pretty = json.dumps(person, indent=4)
print("\nPretty JSON:")
print(json_pretty)

# Sort keys alphabetically
json_sorted = json.dumps(person, indent=2, sort_keys=True)
print("\nSorted keys:")
print(json_sorted)

# -----------------------------------------------
# SECTION 2: json.loads() - JSON string to Python
# -----------------------------------------------

print("\n--- json.loads() ---")

json_string = '{"name": "Alice", "age": 25, "scores": [95, 87, 92], "active": true}'

# Parse JSON string to Python dict
data = json.loads(json_string)
print("Python dict:", data)
print("Type:", type(data))
print("Name:", data["name"])
print("Scores:", data["scores"])

# -----------------------------------------------
# SECTION 3: json.dump() - Write to file
# -----------------------------------------------

print("\n--- json.dump() to file ---")

data = {
    "employees": [
        {"name": "Alice", "department": "Engineering", "salary": 95000},
        {"name": "Bob", "department": "Marketing", "salary": 75000},
        {"name": "Charlie", "department": "Engineering", "salary": 88000}
    ],
    "company": "TechCorp",
    "year": 2024
}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Written to data.json")

# -----------------------------------------------
# SECTION 4: json.load() - Read from file
# -----------------------------------------------

print("\n--- json.load() from file ---")

with open("data.json", "r") as f:
    loaded = json.load(f)

print("Company:", loaded["company"])
print("Employees:")
for emp in loaded["employees"]:
    print(f"  {emp['name']} ({emp['department']}): ${emp['salary']:,}")

# -----------------------------------------------
# SECTION 5: Custom Encoder
# -----------------------------------------------

print("\n--- Custom Encoder ---")

import datetime

# datetime is not JSON serializable by default
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)

record = {
    "name": "Alice",
    "created_at": datetime.datetime(2024, 1, 15, 10, 30, 0)
}

# Use custom encoder
json_output = json.dumps(record, cls=DateTimeEncoder, indent=2)
print(json_output)

# -----------------------------------------------
# SECTION 6: JSON with API data
# -----------------------------------------------

print("\n--- Practical: Processing JSON API data ---")

# Simulate API response
api_response = """
{
  "status": "success",
  "data": {
    "users": [
      {"id": 1, "name": "Alice", "email": "alice@example.com"},
      {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ],
    "total": 2
  }
}
"""

response = json.loads(api_response)
if response["status"] == "success":
    users = response["data"]["users"]
    print(f"Found {response['data']['total']} users:")
    for user in users:
        print(f"  {user['id']}: {user['name']} <{user['email']}>")

# Cleanup
os.remove("data.json")

print("\n" + "="*50)
print("Chapter 54 Complete!")
print("="*50)
