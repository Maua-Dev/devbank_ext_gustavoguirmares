from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item
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


app = FastAPI()

repo = Environments.get_UserData_repo()()

@app.get("/items/get_all_items")
def get_all_items():
    items = repo.get_all_items()
    return {
        "items": [item.to_dict() for item in items]
    }


    


handler = Mangum(app, lifespan="off")