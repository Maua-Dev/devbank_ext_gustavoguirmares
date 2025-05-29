from typing import Dict, Tuple
from ..enums.transaction_type_enum import transactionTypeEnum
from ..errors.entity_errors import ParamNotValidated


class Transaction :
    transaction_type : transactionTypeEnum
    value : float
    current_balance : float
    timestamp : float

    def __init__(self,transaction_type: transactionTypeEnum = None, value: float = None, current_balance: float = None, timestamp: float = None) : 

        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if not validation_transaction_type[0] :
            raise ParamNotValidated("Transatcion type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_value = self.validate_value(value)
        if not validation_value[0] :
            raise ParamNotValidated("Value", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if not validation_current_balance[0] :
            raise ParamNotValidated("current balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if not validation_timestamp[0] :
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp
    
    @staticmethod
    def validate_transaction_type(transaction_type: transactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None :
            return(False, "transaction type is required")
        if not isinstance(transaction_type, transactionTypeEnum):
            return(False, "Transaction type must be Deposit or withdraw")
        return(True, "")
    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str] :
        if value is None :
            return(False, "Value is required")
        if not isinstance(value,float):
            return(False, "Value must be a float")
        if value <= 0 :
            return(False, "Value must be more then 0")
        return(True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if not isinstance(current_balance, float):
            return (False, "Current balance must be a float")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: str) -> tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if not isinstance(timestamp,float) :
            return (False, "Timestamp must be a float")
        return (True, "")

    def to_dict(self) -> Dict:
        return {
    "transaction_type" : self.transaction_type.value,
    "value":  self.value,
    "current_balance" : self.current_balance,
    "timestamp" : self.timestamp

    }