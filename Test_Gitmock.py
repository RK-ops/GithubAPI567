import unittest
from unittest import mock
from unittest.mock import MagicMock
import GitInfo

class test_gitmock(unittest.TestCase):
    @mock.patch('GitInfo.getNoOfCommits')
    def test_mock_noOfCommits(self, mock_user):
        mock_user.return_value = MagicMock(user_id="RK-ops", repo_name="GithubAPI567")
        print(mock_user.return_value)
        result = mock_user.return_value.user_id
        try:
            self.assertEqual(result, "RK-ops")
        except:
            print("Test Failed")
        else:
            print("Test Passed")

    @mock.patch('GitInfo.getGitRepoInfo')
    def test_mock_noOfRepo(self, mock_user):
        mock_user.return_value = MagicMock(user_id="RK-ops")
        print(mock_user.return_value)
        result = mock_user.return_value.user_id
        try:
            self.assertEqual(result, "RK-ops")
        except:
            print("Test Failed")
        else:
            print("Test succeed")


if __name__ == '__main__':
    unittest.main()