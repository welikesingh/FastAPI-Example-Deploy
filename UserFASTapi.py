
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# user.model_dump() is a Pydantic method that converts a Pydantic model object 
# into a Python dictionary (dict).

# Global dictionary for users
user_db_dict = {
    1: {"name": "balwant", "age": 30},
    2: {"name": "amrendra", "age": 25},
    3: {"name": "mustafa", "age": 28}
}


class User(BaseModel):
        name: str
        age: int


# ADD USER
@app.post("/user_db/data/v1/add")
def add_user(user: User):
    if user_db_dict:
        new_user_id = max(user_db_dict.keys()) + 1
    else:
        new_user_id = 1

    user_db_dict[new_user_id] = user.model_dump() 
    # user.model_dump() is a Pydantic method that converts a Pydantic model object 
    # into a Python dictionary (dict).
    return {
        "message": "User added successfully",
        "user_id": new_user_id,
        "user": user_db_dict[new_user_id]
    }


# UPDATE USER
@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id: int, user: User):
    if user_id in user_db_dict:
        user_db_dict[user_id] = user.model_dump()
        # user.model_dump() is a Pydantic method that converts a Pydantic model object 
        # into a Python dictionary (dict).
        return {
            "message": "User updated successfully",
            "user": user_db_dict[user_id]
        }
    else:
        return {"message": "User not found"}


# DELETE USER
@app.delete("/user_db/data/v1/delete/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db_dict:
        del user_db_dict[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}


# GET USER
@app.get("/user_db/data/v1/get/{user_id}")
def get_user(user_id: int):
    if user_id in user_db_dict:
        return {
            "message": "User found successfully",
            "user_id": user_id,
            "user": user_db_dict[user_id]
        }
    else:
        return { "message": "User not found" }

    
# deployment on Render
# pip install -r requirements.txt

# Local run command
# uvicorn UserFASTapi:app --reload

# Render deployment Start command
# uvicorn testing:app --host 0.0.0.0 --port 10000




# https://apitestrender-gjhb.onrender.com/docs
# test API from above link click on put method and thenclick on try out button
# pass user id 1    