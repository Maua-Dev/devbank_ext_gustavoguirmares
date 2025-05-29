from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import transactionTypeEnum
from src.app.repo.transaction_repository_mock import transactionRepositoryMock


class Test_transactionRepositoryMock:

    def test_get_all_transactions(self):
        repo = transactionRepositoryMock()
        transactions = repo.get_all_transactions()
        expected_transactions = repo.transaction
        assert transactions == expected_transactions


    def test_deposit_transaction(self):
        repo = transactionRepositoryMock()

        test_transaction = Transaction(transactionTypeEnum.DEPOSIT,500.0,1500.0,1690482853890.0)
        repo.deposit_transaction(test_transaction)
        transactions = repo.get_all_transactions()
        expected_transactions = repo.transaction
        assert transactions == expected_transactions
        assert test_transaction in transactions


    def test_withdraw_transaction(self):
        repo = transactionRepositoryMock()
        test_transaction = Transaction(transactionTypeEnum.WITHDRAW,300.0,700.0,1690482853890.0)
        repo.withdraw_transaction(test_transaction)
        transactions = repo.get_all_transactions()
        expected_transactions = repo.transaction
        assert transactions == expected_transactions
        assert test_transaction in transactions
