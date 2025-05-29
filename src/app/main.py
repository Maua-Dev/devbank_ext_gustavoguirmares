from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments
from .entities.user import UserData


app = FastAPI()


repo_user = Environments.get_UserData_repo()()

@app.get("/UsersData/get_all_usersData")
def get_all_usersData():
    users_data = repo_user.get_all_usersData()
    return {
        "UsersData": [user.to_dict() for user in users_data]
    }


handler = Mangum(app, lifespan="off")