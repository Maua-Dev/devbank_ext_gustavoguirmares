from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments



from .errors.entity_errors import ParamNotValidated



from .entities.user import UserData


app = FastAPI()

repo = Environments.get_UserData_repo()()

@app.get("/UsersData/get_all_usersData")
def get_all_usersData() :
    UsersData = repo.get_all_usersData()
    UsersData_list = list()
    for UserData in UsersData:
        UsersData_list.append(UserData.to_dict())

    return {
        "UsersData" : UsersData_list
    }
handler = Mangum(app, lifespan="off")
