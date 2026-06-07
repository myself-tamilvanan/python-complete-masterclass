# Chapter 13: Web Services and APIs
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import json
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse

# -----------------------------------------------
# SECTION 1: XML Parsing
# -----------------------------------------------

print("--- XML Parsing ---")

# Sample XML data
xml_data = """<note>
  <to>Alice</to>
  <from>Bob</from>
  <subject>Hello</subject>
  <body>Hi there! Hope you are well.</body>
</note>"""

# Parse XML string
tree = ET.fromstring(xml_data)

# Access elements
print("To:", tree.find("to").text)
print("From:", tree.find("from").text)
print("Subject:", tree.find("subject").text)

# More complex XML
xml_list = """<data>
  <person><name>Alice</name><age>30</age></person>
  <person><name>Bob</name><age>25</age></person>
  <person><name>Charlie</name><age>35</age></person>
</data>"""

root = ET.fromstring(xml_list)
print("\nPeople from XML:")
for person in root.findall("person"):
    name = person.find("name").text
    age = person.find("age").text
    print(f"  {name}, age {age}")

# -----------------------------------------------
# SECTION 2: JSON Parsing
# -----------------------------------------------

print("\n--- JSON Parsing ---")

# Sample JSON string
json_str = '''[
  {"id": 1, "name": "Alice", "score": 95.5},
  {"id": 2, "name": "Bob", "score": 87.0},
  {"id": 3, "name": "Charlie", "score": 92.3}
]''' 

# Parse JSON string to Python object
data = json.loads(json_str)
print("Type:", type(data))     # list
print("First item:", data[0])

# Access values
for item in data:
    print(f"  {item['name']}: {item['score']}")

# -----------------------------------------------
# SECTION 3: Converting Python to JSON
# -----------------------------------------------

print("\n--- Python to JSON ---")

# Python dict to JSON string
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL", "JavaScript"],
    "active": True
}

# json.dumps() converts Python to JSON string
json_output = json.dumps(person, indent=2)
print(json_output)

# -----------------------------------------------
# SECTION 4: Calling a Web API (GeoLocation)
# -----------------------------------------------

print("\n--- Web API Example ---")

def get_geolocation(address):
    """Get latitude/longitude for an address using Google Maps API."""
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
    # Note: In real use, you need an API key
    params = urllib.parse.urlencode({"address": address})
    url = serviceurl + params
    print("Fetching:", url)
    
    try:
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        js = json.loads(data)
        
        if js["status"] != "OK":
            return None
        
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        return lat, lng
    except:
        return None

# Uncomment to run (requires internet):
# result = get_geolocation("Ann Arbor, MI")
# if result:
#     lat, lng = result
#     print(f"Lat: {lat}, Lng: {lng}")

print("API function defined (requires API key to run)")

# -----------------------------------------------
# SECTION 5: Simple Open API Call
# -----------------------------------------------

print("\n--- Open API Example ---")

def fetch_joke():
    """Fetch a random joke from a free API."""
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urllib.request.urlopen(req, timeout=5)
        data = json.loads(response.read().decode())
        return data.get("setup", "") + "\n" + data.get("punchline", "")
    except Exception as e:
        return f"Could not fetch joke: {e}"

# Uncomment to try:
# print(fetch_joke())

# -----------------------------------------------
# SECTION 6: JSON File Handling
# -----------------------------------------------

print("\n--- JSON File Handling ---")

# Save data as JSON file
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A+"}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)
print("Saved students.json")

# Read it back
with open("students.json", "r") as f:
    loaded = json.load(f)
print("Loaded:", loaded)

import os
os.remove("students.json")   # Clean up

print("\n" + "="*50)
print("Chapter 13 Complete!")
print("="*50)