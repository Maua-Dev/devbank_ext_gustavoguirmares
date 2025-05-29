from abc import ABC, abstractmethod
from typing import List

from src.app.entities.transaction import Transaction


class ITransactionRepository(ABC) : 
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction] :
        """
        Return all the transactions in the database 

        """
        pass 
    
    @abstractmethod
    def deposit_transaction(self, transaction : Transaction):
        """
        Create a deposit transaction

        """
        pass

    @abstractmethod
    def withdraw_transaction(self, transaction : Transaction):
        """
        Create a withdraw transaction

        """
        pass