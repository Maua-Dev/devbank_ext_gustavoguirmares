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
    
    if UsersData:
        return UsersData[0].to_dict() 
    else:
        raise HTTPException(status_code=404, detail="No user data found")

def timestamp_time():
    return time.time() * 1000

@app.post("/deposit", status_code=201)
def deposit_transaction(value : float):
    if value is None :
        raise HTTPException(status_code=400, detail="value is required")

    user = repo_user.get_userData_by_name("Gustavo")
    
    if value > user.current_balance * 2:
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    user.current_balance += float(value)
    
    transaction = Transaction(
        transaction_type=transactionTypeEnum.DEPOSIT,
        value=value,
        current_balance=user.current_balance,
        timestamp = timestamp_time()
    )

   
    transaction_register = repo_transactions.deposit_transaction(transaction)

    return {
        "current_balance": user.current_balance,
        "timestamp": timestamp_time()
    }


@app.post("/withdraw", status_code=201) 
def withdraw_transaction(value: float):
    if value <= 0:
        raise HTTPException(status_code=400, detail="Value must be greater than 0 for withdrawal")

    user = repo_user.get_userData_by_name("Gustavo")
    if value > user.current_balance:
        raise HTTPException(status_code=403, detail="Insufficient balance")
    
    user.current_balance -= value 
    
    transaction = Transaction(
        transaction_type=transactionTypeEnum.WITHDRAW, 
        value=value,
        current_balance=user.current_balance,
        timestamp = timestamp_time()

    )

    transaction_register = repo_transactions.withdraw_transaction(transaction) 

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