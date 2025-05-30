from fastapi import FastAPI, HTTPException
from mangum import Mangum
import time

from .entities.transaction import Transaction
from .enums.transaction_type_enum import transactionTypeEnum
from .errors.entity_errors import ParamNotValidated


from .environments import Environments

app = FastAPI()


repo_user = Environments.get_UserData_repo()()
repo_transactions = Environments.get_transactions_repo()()

@app.get("/")
def get_userData(repo=repo_user):
    UsersData = repo.get_userData()
    return {
        "UsersData": [user.to_dict() for user in UsersData]
    }
def timestamp_time():
    return int(time.time() * 1000)

@app.post("/deposit", status_code=201)
def deposit_transaction(request: dict):
    value = request.get("value")
    if value is None :
        raise HTTPException(status_code=400, detail="value is required")

    user = repo_user.get_userData_by_name("Gustavo")
    
    if float(value) > user.current_balance * 2:
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    user.current_balance += float(value)
    
    transaction = Transaction(
        transaction_type=transactionTypeEnum.DEPOSIT,
        value=float(value),
        current_balance=user.current_balance,
        timestamp= timestamp_time()
    )

   
    transaction_register = repo_transactions.deposit_transaction(transaction)

    return {
        "current_balance": user.current_balance,
        "timestamp": timestamp_time()
    }

@app.get("/history")
def get_all_transactions():
    transactions = repo_transactions.get_all_transactions()
    return {
        "transactions": [transaction.to_dict() for transaction in transactions]
    }




handler = Mangum(app, lifespan="off")


