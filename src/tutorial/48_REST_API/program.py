# Chapter 48: REST API with Python
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 11:33:57
# ============================================

import json
import urllib.error
import urllib.request

print("--- REST API with Python ---")

# -----------------------------------------------
# SECTION 1: Consuming REST APIs
# -----------------------------------------------

print("\n--- Consuming REST APIs ---")


def http_get(url, headers=None):
    """Make a GET request."""
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return {"status": resp.status, "data": json.loads(resp.read())}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": str(e)}
    except Exception as e:
        return {"status": -1, "error": str(e)}


# JSONPlaceholder - free test API
url = "https://jsonplaceholder.typicode.com/users?_limit=3"
result = http_get(url)
if result["status"] == 200:
    print("GET users response:")
    for user in result["data"]:
        print(f"  {user['id']}: {user['name']} ({user['email']})")
else:
    print("API unavailable:", result.get("error", "unknown"))
    print("(Internet connection needed for live demo)")

# -----------------------------------------------
# SECTION 2: Using requests library
# -----------------------------------------------

print("\n--- requests library ---")

try:
    import requests

    BASE = "https://jsonplaceholder.typicode.com"

    # GET
    r = requests.get(f"{BASE}/posts", params={"userId": 1, "_limit": 3})
    print(f"GET posts: status={r.status_code}")
    for post in r.json():
        print(f"  [{post['id']}] {post['title'][:40]}...")

    # POST
    r = requests.post(
        f"{BASE}/posts", json={"title": "My Post", "body": "Content here", "userId": 1}
    )
    print(f"\nPOST: status={r.status_code}, id={r.json()['id']}")

    # PUT
    r = requests.put(
        f"{BASE}/posts/1", json={"id": 1, "title": "Updated", "body": "Updated body", "userId": 1}
    )
    print(f"PUT: status={r.status_code}")

    # DELETE
    r = requests.delete(f"{BASE}/posts/1")
    print(f"DELETE: status={r.status_code}")

    # Headers and auth
    headers = {"Authorization": "Bearer my_api_token", "X-API-Version": "v2"}
    r = requests.get(f"{BASE}/users/1", headers=headers)
    print(f"\nWith auth headers: {r.status_code}")

except ImportError:
    print("requests not installed. Run: pip install requests")

# -----------------------------------------------
# SECTION 3: Flask REST API
# -----------------------------------------------

print("\n--- Flask REST API (run separately) ---")

FLASK_CODE = """
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/api/users/<int:uid>", methods=["GET"])
def get_user(uid):
    return jsonify(users.get(uid)) if uid in users else (jsonify({"error": "Not found"}), 404)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = max(users) + 1
    users[new_id] = {"id": new_id, **data}
    return jsonify(users[new_id]), 201

@app.route("/api/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    if uid in users:
        del users[uid]
        return jsonify({"message": "deleted"})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
"""

print("Flask REST API - save as flask_api.py and run with: python3 flask_api.py")
print("Then test with: curl http://localhost:5000/api/users")

# -----------------------------------------------
# SECTION 4: REST Best Practices
# -----------------------------------------------

print("\n--- REST Best Practices ---")

practices = [
    "Use nouns for URLs: /api/users not /api/getUsers",
    "Use HTTP methods for actions: GET=read, POST=create, DELETE=remove",
    "Version your API: /api/v1/users",
    "Return proper status codes: 201 for created, 404 for not found",
    "Paginate large results: ?page=1&limit=20",
    "Use HTTPS in production always",
    "Authenticate with API keys or JWT tokens",
    "Return consistent JSON error format",
]

for i, practice in enumerate(practices, 1):
    print(f"  {i}. {practice}")

print("\n" + "=" * 50)
print("Chapter 48 Complete!")
print("Congratulations! 12-Hour Python Masterclass Complete!")
print("=" * 50)
