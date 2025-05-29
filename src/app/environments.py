
# from enum import Enum
# import os

# from src.app.repo.userData_repository_interface import IUserDataRepository

# from .errors.environment_errors import EnvironmentNotFound



# class STAGE(Enum):
#     DOTENV = "DOTENV"
#     DEV = "DEV"
#     PROD = "PROD"
#     TEST = "TEST"


# class Environments:
#     """
#     Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

#     Usage:

#     """
#     stage: STAGE

#     def _configure_local(self):
#         from dotenv import load_dotenv
#         load_dotenv()
#         os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

#     def load_envs(self):
#         if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
#             self._configure_local()

#         self.stage = STAGE[os.environ.get("STAGE")]

#     @staticmethod
#     def get_UserData_repo() -> IUserDataRepository:
#         if Environments.get_envs().stage == STAGE.TEST:
#             from .repo.userData_repository_mock import UserDataRepositoryMock 
#             return UserDataRepositoryMock
#         # use "elif" conditional to add other stages
#         else:
#             raise EnvironmentNotFound("STAGE")
        

#     @staticmethod
#     def get_envs() -> "Environments":
#         """
#         Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
#         :return: Environments (stage={self.stage})

#         """
#         envs = Environments()
#         envs.load_envs()
#         return envs

#     def __repr__(self):
#         return self.__dict__

#-------- teste


from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/items/get_all_items")
def get_all_items():
    items = repo.get_all_items()
    return {
        "items": [item.to_dict() for item in items]
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    return {
        "item_id": item_id,
        "item": item.to_dict()    
    }

@app.post("/items/create_item", status_code=201)
def create_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    if item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    
    name = request.get("name")
    price = request.get("price")
    item_type = request.get("item_type")
    if item_type is None:
        raise HTTPException(status_code=400, detail="Item type is required")
    if type(item_type) != str:
        raise HTTPException(status_code=400, detail="Item type must be a string")
    if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
        raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
    admin_permission = request.get("admin_permission")
    
    try:
        item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    item_response = repo.create_item(item, item_id)
    return {
        "item_id": item_id,
        "item": item_response.to_dict()    
    }
    
@app.delete("/items/delete_item")
def delete_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    item_deleted = repo.delete_item(item_id)
    
    return {
        "item_id": item_id,
        "item": item_deleted.to_dict()    
    }
    
@app.put("/items/update_item")
def update_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    name = request.get("name")
    price = request.get("price")
    admin_permission = request.get("admin_permission")
    
    item_type_value = request.get("item_type")
    if item_type_value != None:
        if type(item_type_value) != str:
            raise HTTPException(status_code=400, detail="Item type must be a string")
        if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
            raise HTTPException(status_code=400, detail="Item type is not a valid one")
        item_type = ItemTypeEnum[item_type_value]
    else:
        item_type = None
        
    item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
    return {
        "item_id": item_id,
        "item": item_updated.to_dict()    
    }
    


handler = Mangum(app, lifespan="off")