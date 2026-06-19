# Chapter 38: Generator & Yield (Deep Dive)
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:50:24
# ============================================


print("--- Generator Deep Dive ---")

# -----------------------------------------------
# SECTION 1: yield basics
# -----------------------------------------------


def countdown(n):
    """Generator: counts down from n."""
    while n > 0:
        yield n
        n -= 1


gen = countdown(5)
print("Countdown:", list(gen))

# -----------------------------------------------
# SECTION 2: yield from
# -----------------------------------------------

print("\n--- yield from ---")


def flatten(nested):
    """Recursively flatten using yield from."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = [1, [2, [3, 4]], [5, 6], 7]
print("Flattened:", list(flatten(data)))

# -----------------------------------------------
# SECTION 3: Infinite Generator
# -----------------------------------------------

print("\n--- Infinite Generator ---")


def id_generator(start=1):
    """Generate unique IDs forever."""
    while True:
        yield start
        start += 1


ids = id_generator(100)
print("IDs:", [next(ids) for _ in range(5)])

# -----------------------------------------------
# SECTION 4: send() to Generator
# -----------------------------------------------

print("\n--- send() ---")


def accumulator():
    """Accept values via send() and return running sum."""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


acc = accumulator()
next(acc)  # Prime the generator
print("Running totals:")
for v in [10, 20, 30, 5]:
    result = acc.send(v)
    print(f"  After adding {v}: {result}")

# -----------------------------------------------
# SECTION 5: Generator Pipeline (ETL)
# -----------------------------------------------

print("\n--- Generator Pipeline ---")


def read_data(n):
    """Source: generate raw data."""
    for i in range(n):
        yield {"id": i, "value": i * 3 - 5, "label": f"item_{i}"}


def filter_positive(records):
    """Filter: keep positive values."""
    for rec in records:
        if rec["value"] > 0:
            yield rec


def transform(records):
    """Transform: add category field."""
    for rec in records:
        rec["category"] = "high" if rec["value"] > 10 else "low"
        yield rec


def to_summary(records):
    """Sink: produce summary."""
    for rec in records:
        yield f"{rec['label']}: {rec['value']} ({rec['category']})"


# Build the pipeline (lazy - nothing computed yet)
pipeline = to_summary(transform(filter_positive(read_data(20))))

print("Pipeline results:")
for line in pipeline:
    print(f"  {line}")

print("\n" + "=" * 50)
print("Chapter 38 Complete!")
print("=" * 50)
