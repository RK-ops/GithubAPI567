import unittest
from unittest.mock import patch
import GitHubApi


class TestGetHub(unittest.TestCase):

    @patch("GitHubApi.getrepo")
    def testConnection1(self, mock_connect):
        mock_connect.return_value = [200, {"Triangle567", "Testing-triangle-classification", "Guess-a-Number", "hello-world","HW-05_Static-Code-Analysis"}]
        self.assertTrue(GitHubApi.getrepo("RK-ops")[0])

    @patch("GitHubApi.getrepo")
    def test_repos1(self, mock_connect):
        mock_connect.return_value = [200, {"Triangle567", "Testing-triangle-classification", "Guess-a-Number", "hello-world","HW-05_Static-Code-Analysis"}]
        self.assertIs(mock_connect()[1], GitHubApi.getrepo("RK-ops")[1])

    @patch("GitHubApi.getrepo")
    def testConnection2(self, mock_connect):
        mock_connect.return_value = [200, {""}]
        self.assertTrue(GitHubApi.getrepo("RK-ops")[0])

    @patch("GitHubApi.getrepo")
    def test_repos2(self, mock_connect):
        mock_connect.return_value = [200, {""}]
        self.assertIs(mock_connect()[1], GitHubApi.getrepo("RK-ops")[1])


if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetHub)
    unittest.TextTestRunner(verbosity=2).run(suite)
