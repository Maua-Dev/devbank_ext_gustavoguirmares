from src.app import repo
from src.app.entities.user import UserData
from src.app.repo.userData_repository_mock import UserDataRepositoryMock

class TestUserDataRepositoryMock:
    def test_get_userData(self):
        repo = UserDataRepositoryMock()
        user_data = repo.get_userData()
        expected_user = repo.UsersData[0]
        assert user_data == expected_user

    
    def test_get_userData_by_name(self):
        repo = UserDataRepositoryMock()
        user = repo.get_userData_by_name("Gustavo") 
        assert user is not None
        assert user.name == "Gustavo"

    

