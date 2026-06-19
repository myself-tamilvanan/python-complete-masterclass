# Chapter 50: Collections Module
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

from collections import Counter, OrderedDict, defaultdict, deque, namedtuple

# -----------------------------------------------
# SECTION 1: Counter
# -----------------------------------------------

print("--- Counter ---")

a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(2))
print(list(my_counter.elements()))

# Counter arithmetic
c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
print("Add:", c1 + c2)
print("Sub:", c1 - c2)

# -----------------------------------------------
# SECTION 2: namedtuple
# -----------------------------------------------

print("\n--- namedtuple ---")

Point = namedtuple("Point", ["x", "y"])
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

Employee = namedtuple("Employee", "name department salary")
emp = Employee("Alice", "Engineering", 95000)
print(emp.name, emp.department, emp.salary)

# -----------------------------------------------
# SECTION 3: OrderedDict
# -----------------------------------------------

print("\n--- OrderedDict ---")

od = OrderedDict()
od["b"] = 2
od["a"] = 1
od["c"] = 3
print(od)

od.move_to_end("a")
print("After move_to_end:", od)

# -----------------------------------------------
# SECTION 4: defaultdict
# -----------------------------------------------

print("\n--- defaultdict ---")

# int default (0)
dd_int = defaultdict(int)
dd_int["a"] += 1
dd_int["b"] += 5
print("defaultdict(int):", dict(dd_int))

# list default
dd_list = defaultdict(list)
dd_list["key1"].append("value1")
dd_list["key1"].append("value2")
dd_list["key2"].append("value3")
print("defaultdict(list):", dict(dd_list))

# Grouping with defaultdict
students = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Science")]
groups = defaultdict(list)
for name, subject in students:
    groups[name].append(subject)
print("Grouped:", dict(groups))

# -----------------------------------------------
# SECTION 5: deque
# -----------------------------------------------

print("\n--- deque ---")

d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print("deque:", d)

d.pop()
d.popleft()
print("After pops:", d)

# maxlen sliding window
d = deque(maxlen=3)
for i in range(6):
    d.append(i)
    print("  Window:", list(d))

# rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print("Rotated right 2:", list(d))

print("\n" + "=" * 50)
print("Chapter 50 Complete!")
print("=" * 50)
