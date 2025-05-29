from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

app = FastAPI()

repo = Environments.get_UserData_repo()()

@app.get("/UsersData/get_all_usersData")
def get_all_usersData():
    UsersData = repo.get_all_usersData()
    return {
        "UsersData": [user.to_dict() for user in UsersData]
    }

@app.get("/UsersData/get_userData_by_name")
def get_userData_by_name(name: str):
    user = repo.get_userData_by_name(name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "name": name,
        "UserData": user.to_dict()
    }


handler = Mangum(app, lifespan="off")


