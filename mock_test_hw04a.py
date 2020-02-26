"""
Date: 02/26/2020
Author:Tiancheng Xu
Homework 05a mock test

Test the 04a file with Mock
"""
import unittest
from unittest import mock
import HW04a_txu
from HW04a_txu import get_user_ID, get_user_repo, get_user_commit

class test_hw04a_mock(unittest.TestCase):
    
    @mock.patch('requests.get')
    def test_repo(self, mock_repo):
        mock_repo.return_value.json.return_value = [
            {"name": "666"}, 
            {"name": "CS570"},
            {"name": "GitHubApi567"},
            {"name": "SSW567"}, 
            {"name": "SSW810"},
            {"name": "StarbucksAnalysis"},
            {"name": "txu567"}]
        self.assertEqual(get_user_repo('weichen66'), ['666','CS570','GitHubApi567','SSW567','SSW810','StarbucksAnalysis','txu567'])

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)