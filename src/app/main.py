from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

app = FastAPI()

repo_user = Environments.get_UserData_repo()()

@app.get("/")
def get_all_usersData():
    UsersData = repo_user.get_all_usersData()
    return {
        "UsersData": [user.to_dict() for user in UsersData]
    }

@app.get("/UsersData/get_userData_by_name")
def get_userData_by_name(name: str):
    userData = repo_user.get_userData_by_name(name)
    if userData is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
         "UsersData": [user.to_dict() for user in userData]
    }

@app.get("/UsersData/get_userData_by_agency_or_account")
def get_userData_by_agency_and_account(agency: str, account: str):
    userData = repo_user.get_userData_by_agency_and_account(agency, account)
    if userData is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
       "UsersData": [user.to_dict() for user in userData] 
    }

handler = Mangum(app, lifespan="off")


