from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import List

app = FastAPI()

# Load CSV
def load_csv():
    try:
        data = pd.read_csv("data/SehiBukhariHadees.csv")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading CSV: {str(e)}")

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CSV Example!"}

@app.get("/users")
async def get_users():
    try:
        data = load_csv()
        users = data.to_dict(orient="records")
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        data = load_csv()
        user = data[data["id"] == user_id]
        if user.empty:
            raise HTTPException(status_code=404, detail="User not found")
        return user.to_dict(orient="records")[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
