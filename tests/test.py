
import sys
import os
import unittest

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

import progress_bar

from progress_bar import ProgressBar
from progress_bar.exceptions import ProgressBarNumberError, ProgressBarIntegerNumberError, ProgressBarHigherNumberError


class TestProgressBar(unittest.TestCase):

    def test_negative(self):
        bar = ProgressBar()
        self.assertRaises(
            ProgressBarNumberError,
            bar.load, 
            end=-1
        )

    def test_number_100(self):
        bar = ProgressBar()
        self.assertRaises(
            ProgressBarNumberError,
            bar.load, 
            end=101
        )

    def test_number_string(self):
        bar = ProgressBar()
        self.assertRaises(
            ProgressBarIntegerNumberError,
            bar.load, 
            end='1'
        )

    def test_numbers(self):
        bar = ProgressBar()
        self.assertRaises(
            ProgressBarHigherNumberError,
            bar.load, 
            start=10,
            end=0,
        )

if __name__ == '__main__':
    unittest.main()