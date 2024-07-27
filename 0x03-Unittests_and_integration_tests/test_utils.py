#!/usr/bin/env python3
"""test utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test the access_nested_map function with different inputs and expected
        outputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_error):
        """
        Test the access_nested_map function with different inputs and expected
        outputs.
        """
        with self.assertRaises(expected_error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function under test
            result = get_json(test_url)

            # Assertions
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)
