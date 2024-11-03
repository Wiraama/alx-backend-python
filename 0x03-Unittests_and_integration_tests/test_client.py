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

            self.assertEqual(client._public_repos_url, payload["repos_url"]
