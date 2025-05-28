import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import transactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_transaction :
    def test_transaction(self):
        transaction = Transaction(transactionTypeEnum.DEPOSIT,123.0,500.0,1690482853890.0)
        assert transaction.transaction_type == transactionTypeEnum.DEPOSIT
        assert transaction.value == 123.0
        assert transaction.current_balance == 500.0
        assert transaction.timestamp == 1690482853890.0

    def test_transaction_type_is_none(self) :
        with pytest.raises(ParamNotValidated) :
            Transaction(123.0,500.0,1690482853890.0)
        
    def test_transaction_type_is_transactionTypeEnum(self):
        with pytest.raises(ParamNotValidated):
            Transaction("deposit",123.0,500.0,1690482853890.0)

    def test_value_is_none(self) : 
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,500.0,1690482853890.0)

    def test_value_is_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transactionTypeEnum.DEPOSIT,"123.0",500.0,1690482853890.0)

    def test_value_more_then_0(self):
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,-2,500.0,1690482853890.0)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,123.0,1690482853890.0)

    def test_current_balance_is_float(self):
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,123.0,"500.0",1690482853890.0)

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,123.0,500.0)

    def test_timestamp_is_float(self):
        with pytest.raises(ParamNotValidated) :
            Transaction(transactionTypeEnum.DEPOSIT,123.0,500.0,"1690482853890.0")


    def test_to_dict_transaction(self):
        transaction_type=transactionTypeEnum.DEPOSIT
        value=123.0
        current_balance=500.0
        timestamp=1690482853890.0

        transaction = Transaction(transaction_type,value,current_balance,timestamp)

        transaction_dict = transaction.to_dict()

        expected_transaction_dict = {
            "transaction_type" : transactionTypeEnum.DEPOSIT.value,
            "value" : value,
            "current_balance" : current_balance,
            "timestamp" : timestamp

        }
        
        assert transaction_dict == expected_transaction_dict

 
