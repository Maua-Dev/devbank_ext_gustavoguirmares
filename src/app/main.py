from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments



from .errors.entity_errors import ParamNotValidated



from .entities.user import UserData


app = FastAPI()

repo = Environments.get_UserData_repo()()


handler = Mangum(app, lifespan="off")
