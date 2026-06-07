# Chapter 45: Flask Web Development
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:43:00
# ============================================
# Run: pip install flask && python3 program.py

try:
    from flask import Flask, request, jsonify, render_template_string
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False
    print("Flask not installed. Run: pip install flask")

if HAS_FLASK:
    # -----------------------------------------------
    # BASIC FLASK APPLICATION
    # -----------------------------------------------
    
    app = Flask(__name__)
    
    # In-memory database (use real DB in production)
    users_db = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25},
        3: {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 35},
    }
    
    # -----------------------------------------------
    # SECTION 1: Basic Routes
    # -----------------------------------------------
    
    @app.route("/")
    def home():
        """Home page."""
        html = """
        <html><body>
        <h1>Flask API Server</h1>
        <p>Endpoints:</p>
        <ul>
            <li>GET /api/users - List all users</li>
            <li>GET /api/users/&lt;id&gt; - Get user by ID</li>
            <li>POST /api/users - Create user</li>
            <li>PUT /api/users/&lt;id&gt; - Update user</li>
            <li>DELETE /api/users/&lt;id&gt; - Delete user</li>
            <li>GET /api/greet/&lt;name&gt; - Greet someone</li>
        </ul>
        </body></html>
        """
        return html
    
    @app.route("/api/greet/<name>")
    def greet(name):
        """Dynamic URL parameter example."""
        return jsonify({"message": f"Hello, {name}!", "status": "success"})
    
    # -----------------------------------------------
    # SECTION 2: REST API - CRUD Operations
    # -----------------------------------------------
    
    @app.route("/api/users", methods=["GET"])
    def get_users():
        """Get all users with optional filtering."""
        age_min = request.args.get("age_min", type=int)
        users = list(users_db.values())
        if age_min:
            users = [u for u in users if u["age"] >= age_min]
        return jsonify({"users": users, "count": len(users)})
    
    @app.route("/api/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        """Get a single user by ID."""
        user = users_db.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user)
    
    @app.route("/api/users", methods=["POST"])
    def create_user():
        """Create a new user."""
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "name is required"}), 400
        new_id = max(users_db.keys()) + 1 if users_db else 1
        user = {"id": new_id, "name": data["name"],
                "email": data.get("email", ""), "age": data.get("age", 0)}
        users_db[new_id] = user
        return jsonify(user), 201
    
    @app.route("/api/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        """Update a user."""
        if user_id not in users_db:
            return jsonify({"error": "User not found"}), 404
        data = request.get_json()
        users_db[user_id].update(data)
        return jsonify(users_db[user_id])
    
    @app.route("/api/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        """Delete a user."""
        if user_id not in users_db:
            return jsonify({"error": "User not found"}), 404
        deleted = users_db.pop(user_id)
        return jsonify({"message": f"Deleted {deleted['name']}"})
    
    # -----------------------------------------------
    # SECTION 3: Error Handlers
    # -----------------------------------------------
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500
    
    # -----------------------------------------------
    # RUN THE APP
    # -----------------------------------------------
    
    if __name__ == "__main__":
        print("Starting Flask server...")
        print("Visit: http://localhost:5000")
        print("API: http://localhost:5000/api/users")
        app.run(host="0.0.0.0", port=5000, debug=True)

else:
    print("Flask not available. Install with: pip install flask")

print("\n" + "="*50)
print("Chapter 45 Complete!")
print("="*50)