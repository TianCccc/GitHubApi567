"""
Date: 02/18/2020
Author:Tiancheng Xu
Homework 04a Test

Requirements:
Testcase
"""
import unittest
from HW04a_txu import get_user_ID, get_user_repo, get_user_commit

class Testrepocommit(unittest.TestCase):    
    def test_repo1(self):
        self.assertIn("666", get_user_repo("weichen66"))
    def test_repo2(self):
        self.assertIn("CS570", get_user_repo("weichen66"))
    def test_repo3(self):
        self.assertIn("SSW567", get_user_repo("weichen66"))
    def test_repo4(self):
        self.assertIn("SSW810", get_user_repo("weichen66"))    
    def test_repo5(self):
        self.assertIn("StarbucksAnalysis", get_user_repo("weichen66"))
    def test_repo6(self):
        self.assertIn("txu567", get_user_repo("weichen66"))

    def test_commits1(self):
        self.assertEqual(1, get_user_commit("weichen66", "666"))
    def test_commits2(self):
        self.assertEqual(1, get_user_commit("weichen66", "CS570"))
    def test_commits3(self):
        self.assertEqual(2, get_user_commit("weichen66", "SSW567"))
    def test_commits4(self):
        self.assertEqual(1, get_user_commit("weichen66", "SSW810"))
    def test_commits5(self):
        self.assertEqual(30, get_user_commit("weichen66", "StarbucksAnalysis"))
    def test_commits6(self):
        self.assertEqual(6, get_user_commit("weichen66", "txu567"))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    