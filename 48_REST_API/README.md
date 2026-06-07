# Chapter 48: REST API with Python

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 11:33:57

## Overview
REST (Representational State Transfer) is the most common API architecture. This chapter covers consuming REST APIs with requests library and building them with Flask.

## HTTP Methods and CRUD
| Method | CRUD   | Example URL    | Description        |
|--------|--------|----------------|--------------------|
| GET    | Read   | /api/users     | Get all users      |
| GET    | Read   | /api/users/1   | Get specific user  |
| POST   | Create | /api/users     | Create new user    |
| PUT    | Update | /api/users/1   | Replace user       |
| PATCH  | Update | /api/users/1   | Partial update     |
| DELETE | Delete | /api/users/1   | Delete user        |

## HTTP Status Codes
| Code | Meaning                |
|------|------------------------|
| 200  | OK                     |
| 201  | Created                |
| 400  | Bad Request            |
| 401  | Unauthorized           |
| 404  | Not Found              |
| 500  | Internal Server Error  |

## Installation
```bash
pip install requests flask
```

## Learning Outcomes
- Consume REST APIs with requests library
- Handle authentication (API keys, Bearer tokens)
- Build REST APIs with Flask
- Handle errors and implement pagination