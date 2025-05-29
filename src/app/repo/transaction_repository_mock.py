from typing import List
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import transactionTypeEnum
from src.app.repo.transaction_repository_interface import ITransactionRepository


class transactionRepositoryMock(ITransactionRepository) :
    transaction : List[Transaction]

    def __init__(self) :
        self.transaction = [
            Transaction(transactionTypeEnum.DEPOSIT, 100.0,500.0,1690482853890.0),
            Transaction(transactionTypeEnum.WITHDRAW, 50.0,500.0,1690482853890.0),
            Transaction(transactionTypeEnum.DEPOSIT, 10.0,500.0,1690482853890.0),
            Transaction(transactionTypeEnum.WITHDRAW, 200.0,500.0,1690482853890.0)

        ]

    def get_all_transactions(self) -> List[Transaction] :
        return self.transaction
    
    def deposit_transaction(self, transaction: Transaction):
        self.transaction.append(transaction)
        return transaction
    
    def withdraw_transaction(self, transaction: Transaction):
        self.transaction.append(transaction)
        return transaction

        
        