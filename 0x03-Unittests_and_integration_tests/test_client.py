#!/usr/bin/env python3
""" modue to test git hub """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to """


    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ method to test GithubOrgClient.org returns the correct value. """
        expected = {"login": org_name}
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """ turns method to properties """
        payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        with.patch.object(GithubOrgClient, "org", new_callable=PropertyMock, return_value=payload):
            client = GithubOrgClient("test_org")

            self.assertEqual(client._public_repos_url, payload["repos_url"])


    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repository names."""
        repos_payload = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"}
            ]
        mock_get_json.return_value = repos_payload

        repos_url = "https://api.github.com/orgs/test_org/repos"

        with patck.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock, return_value=repos_url):
            client = GithubOrgClient("test_org")

            result = client.public_repos

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)
            client._public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)
