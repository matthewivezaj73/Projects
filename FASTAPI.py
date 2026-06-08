# Import FastAPI class → this is the core object that creates your API server
from fastapi import FastAPI

# Import BaseModel → used for request validation + structured JSON bodies
from pydantic import BaseModel

# Create an instance of FastAPI
# This object will hold all your routes (API endpoints)
app = FastAPI()

# ---------------------------
# 1. BASIC GET ENDPOINT
# ---------------------------

# @app.get("/") means:
# "When someone visits the root URL '/', run this function"
@app.get("/")
def home():
    # Returning a Python dictionary automatically becomes JSON
    # FastAPI converts this to HTTP response for you
    return {"message": "API is running"}

# ---------------------------
# 2. PATH PARAMETERS
# ---------------------------

# {user_id} is part of the URL path
# Example: /user/123
# FastAPI automatically extracts it and passes it into the function
@app.get("/user/{user_id}")
def get_user(user_id: int):
    # The ": int" enforces type validation automatically
    # If someone sends "abc", FastAPI rejects the request
    return {"user_id": user_id}

# ---------------------------
# 3. QUERY PARAMETERS
# ---------------------------

# Query parameters come from the URL after ?
# Example: /search?q=ai&limit=5
@app.get("/search")
def search(q: str, limit: int = 5):
    # q is required (no default)
    # limit has a default value, so it's optional
    return {
        "query": q,
        "limit": limit
    }

# ---------------------------
# 4. REQUEST BODY (POST)
# ---------------------------

# BaseModel defines the structure of incoming JSON data
# This is VERY important in real APIs (validation + safety)
class Item(BaseModel):
    name: str      # must be a string
    price: float   # must be a number (float)

# POST means you're sending data to the server
@app.post("/item")
def create_item(item: Item):
    # FastAPI automatically:
    # - parses JSON body
    # - validates types
    # - converts into Item object

    # item.name and item.price are safely accessible here
    return {
        "received": item,   # FastAPI converts it back to JSON
        "status": "created"
    }