from src.app.repo.userData_repository_mock import IUserDataRepositoryMock


class Test_userDataRepositoryMock:
    def test_get_all_usersData(self) :
        repo = IUserDataRepositoryMock()

        UsersData = repo.get_all_usersData()

        expected_userData = repo.UsersData

        assert expected_userData == UsersData

        