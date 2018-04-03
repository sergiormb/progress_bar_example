# -*- coding: utf-8 -*-
from __future__ import print_function

from .exceptions import (
                            ProgressBarNumberError,
                            ProgressBarHigherNumberError,
                            ProgressBarIntegerNumberError,
                        )
import sys
from time import sleep

MILISECONDS = 0.5


class ProgressBar(object):
    """Returns a progress bar.
    Args:
        point: Character to print
    """

    def __init__(self, point='='):
        self.point = point

    def __clean_number(self, number):
        """Clean number.
        Raises:
            ProgressBarIntegerNumberError -- It must be an int
            ProgressBarNumberError -- It must be an integer between 0 and 100
        """
        if not isinstance(number, int):
            raise ProgressBarIntegerNumberError(number)
        if number < 0 or number > 100:
            raise ProgressBarNumberError(number)

    def __clean(self, start, end):
        """Validate all data.
        Raises:
            ProgressBarHigherNumberError -- The start higger than the end
        """
        self.__clean_number(start)
        self.__clean_number(end)
        if start >= end:
            raise ProgressBarHigherNumberError()

    def load(self, start=0, end=100):
        """Initialize the progress bar.
        Keyword Arguments:
            start {int} -- Start of the bar (default: {0})
            end {int} -- End of the bar (default: {100})
        """
        self.__clean(start, end)
        for iteration in self.__print_bar(start, end):
            sleep(MILISECONDS)

    def __print_bar(self, start, total, with_spaces=False):
        """Print the progress bar.
        Arguments:
            start {int} -- Start of the bar
            end {int} -- End of the bar
        Keyword Arguments:
            with_spaces {bool} -- Fill the entire progress bar with spaces
        """
        index = start
        while index <= total:
            done = self.point.encode("utf-8") * (index)
            todo = ''
            if with_spaces:
                todo = ' ' * (total - index - 1)
            s = '[{0}] {1!s}%'.format(done + todo, str(index))
            if index > 0:
                s = '\r' + s
            if not todo and with_spaces:
                s += '\n'
            if index == total:
                s += '\n'
            print(s, end='')
            sys.stdout.flush()
            yield index
            index += 1
