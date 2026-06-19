# Chapter 16: Data Visualization
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import collections
import json
import sqlite3

# -----------------------------------------------
# SECTION 1: Simple Data Analysis and Stats
# -----------------------------------------------

print("--- Data Analysis Basics ---")

# Sample email data for analysis
email_log = [
    ("alice@example.com", "2024-01-05", "Python tutorial"),
    ("bob@test.org", "2024-01-06", "Re: Python tutorial"),
    ("alice@example.com", "2024-01-07", "Data Science"),
    ("charlie@domain.net", "2024-01-08", "Re: Data Science"),
    ("bob@test.org", "2024-01-09", "Machine Learning"),
    ("alice@example.com", "2024-01-10", "Re: Machine Learning"),
    ("diana@uni.edu", "2024-01-11", "Python tutorial"),
]

# Count emails by sender
sender_count = collections.Counter(email[0] for email in email_log)
print("Emails per sender:")
for sender, count in sender_count.most_common():
    print(f"  {sender}: {count}")

# -----------------------------------------------
# SECTION 2: PageRank Algorithm
# -----------------------------------------------

print("\n--- PageRank Algorithm ---")


# Simplified PageRank implementation
def compute_pagerank(links, damping=0.85, iterations=20):
    """
    Compute PageRank for a set of pages.
    links: dict of {page: [list of pages it links to]}
    damping: damping factor (0.85 is standard)
    """
    pages = set(links.keys())
    for targets in links.values():
        pages.update(targets)

    n = len(pages)
    # Initialize all pages with equal rank
    rank = {page: 1 / n for page in pages}

    for _ in range(iterations):
        new_rank = {}
        for page in pages:
            # Sum ranks from all pages linking to this page
            incoming_rank = sum(
                rank[src] / len(targets) for src, targets in links.items() if page in targets
            )
            new_rank[page] = (1 - damping) / n + damping * incoming_rank
        rank = new_rank

    return rank


# Sample web graph
web_graph = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}

pr = compute_pagerank(web_graph)
print("PageRank scores:")
for page, score in sorted(pr.items(), key=lambda x: x[1], reverse=True):
    print(f"  Page {page}: {score:.4f}")

# -----------------------------------------------
# SECTION 3: Matplotlib Visualization
# -----------------------------------------------

print("\n--- Matplotlib Charts ---")

try:
    import matplotlib.pyplot as plt

    # Sample data
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [150, 230, 180, 290, 320, 410]

    # Line plot
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(months, sales, marker="o", color="blue")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.grid(True)

    # Bar chart
    plt.subplot(1, 2, 2)
    plt.bar(months, sales, color="green")
    plt.title("Sales Bar Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")

    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.close()
    print("Chart saved as sales_chart.png")

except ImportError:
    print("matplotlib not installed. Run: pip install matplotlib")

# -----------------------------------------------
# SECTION 4: Email Analysis with Database
# -----------------------------------------------

print("\n--- Email Analysis with Database ---")

# Store email data in SQLite
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Emails (
        id INTEGER PRIMARY KEY,
        sender TEXT,
        date TEXT,
        subject TEXT
    )
""")

# Insert sample data
for i, (sender, date, subject) in enumerate(email_log):
    cur.execute("INSERT INTO Emails VALUES (?, ?, ?, ?)", (i + 1, sender, date, subject))
conn.commit()

# Analyze: most active senders
cur.execute("""
    SELECT sender, COUNT(*) as count
    FROM Emails
    GROUP BY sender
    ORDER BY count DESC
""")

print("Most active senders (from DB):")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]} emails")

conn.close()

# -----------------------------------------------
# SECTION 5: GeoData Processing
# -----------------------------------------------

print("\n--- GeoData Processing ---")

# Sample GeoJSON-like data
locations = [
    {"name": "Ann Arbor", "lat": 42.2808, "lon": -83.7430},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
]

# Convert to GeoJSON format
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [loc["lon"], loc["lat"]]},
            "properties": {"name": loc["name"]},
        }
        for loc in locations
    ],
}

print("GeoJSON features:")
for feature in geojson["features"]:
    name = feature["properties"]["name"]
    coords = feature["geometry"]["coordinates"]
    print(f"  {name}: lon={coords[0]}, lat={coords[1]}")

# Save to file
with open("locations.geojson", "w") as f:
    json.dump(geojson, f, indent=2)
print("\nSaved locations.geojson")

import os

os.remove("locations.geojson")

print("\n" + "=" * 50)
print("Chapter 16 Complete!")
print("Congratulations - Python for Everybody Course Complete!")
print("=" * 50)
