import os
from config import db
from models import User, Task

# Data to initalise database with
USER = [
        {"username": "Will", "password": "1234"},
        {"username": "ABC", "password": "1248"},
        {"username": "XYZ", "password": "5678"}
]

TASK = [
        {"user_id": 1, "title": "Read book", "description": "Harry Potter", "archive": 0},
        {"user_id": 2, "title": "Read book", "description": "Hunger Games", "archive": 1},
        {"user_id": 2, "title": "Make game", "description": "Space fling", "archive": 1}
]

# Delete database file if it exists currently
if os.path.exists("task.db"):
    os.remove("task.db")
    
# Create the database
db.create_all()

# iterate over the USER structure and populate the database
for user in USER:
    u = User(username=user.get("username"), password=user.get("password"))
    db.session.add(u)

# iterate over the TASK structure and populate the database
for task in TASK:
    t = Task(user_id=task.get("user_id"), title=task.get("title"), description=task.get("description"), archive=task.get("archive"))
    db.session.add(t)

db.session.commit()