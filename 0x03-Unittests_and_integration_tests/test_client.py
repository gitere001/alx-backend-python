#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test the `GithubOrgClient` class."""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        """
        Test the `org` method of the `GithubOrgClient` class.

        This test case verifies that the `org` method of the `GithubOrgClient`
        class correctly calls the `get_json` function with the expected URL.

        Parameters:
            name (str): The name of the GitHub organization.
            mock (MagicMock): A mock object of the `get_json` function.

        Returns:
            None

        Raises:
            AssertionError: If the `get_json` function is not called once with
            the expected URL.
        """
        test_class = GithubOrgClient(name)
        test_class.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the `_public_repos_url` method of the `GithubOrgClient` class.

        This test case verifies that the `_public_repos_url` method of the
        `GithubOrgClient`
        class returns the expected URL.

        Parameters:
            self (TestGithubOrgClient): The test case instance.
            mock_org (PropertyMock): A mock object of the `org` method.

        Returns:
            None

        Raises:
            AssertionError: If the `_public_repos_url` method does not return
            the expected URL.
        """
        # Mock the return value of the org method
        mock_org.return_value = {"repos_url": "https://api.github.coms"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test")

        self.assertEqual(client._public_repos_url, "https://api.github.coms")

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        this method unit-test GithubOrgClient.public_repos
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)

            mock_public.assert_called_once()
            mock_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
