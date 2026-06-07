# Chapter 45: Flask Web Development

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:43:00

## Overview
Flask is a lightweight and flexible Python web framework. It is perfect for building REST APIs, web applications, and microservices.

## Installation
```bash
pip install flask
pip install flask-restful   # For REST APIs
```

## Running Flask
```bash
python3 app.py
# or
flask run
```

## Core Concepts
| Concept      | Description                                    |
|--------------|------------------------------------------------|
| Route        | Map URL to function with @app.route()          |
| View function| Python function handling a request             |
| Request      | Access form data, args, headers (flask.request)|
| Response     | Return data (string, HTML, JSON)               |
| Template     | HTML files with Jinja2 templating              |
| Blueprint    | Organize routes into modules                   |

## HTTP Methods
| Method  | Purpose                     |
|---------|-----------------------------|
| GET     | Retrieve data               |
| POST    | Create new resource         |
| PUT     | Update existing resource    |
| DELETE  | Delete resource             |

## Learning Outcomes
- Create Flask web applications
- Define routes and view functions
- Handle GET and POST requests
- Return HTML and JSON responses
- Build a simple REST API