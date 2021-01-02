## @file calcpy/tests.py
#  @brief c++ calculation library Python API unit testing

import time
import django.test

from . import conway
from . import views


class ConwayPyLibraryTestCase(django.test.TestCase):
    """integration test, call C++ library interface from Python"""

    def test01evolve(self):
        """test the return number"""
        blinker_vertical = [
            [False, True, False],
            [False, True, False],
            [False, True, False],
        ]
        blinker_horizontal = [
            [False, False, False],
            [True,  True,  True],
            [False, False, False],
        ]
        self.assertEqual( conway.evolve(blinker_vertical), blinker_horizontal )


class ConwayPyViewTestCase(django.test.TestCase):
    """module view test"""

    def test01getNumber(self):
        """check if service return proper dict"""
        blinker_vertical = [
            [False, True, False],
            [False, True, False],
            [False, True, False],
        ]
        blinker_horizontal = [
            [False, False, False],
            [True,  True,  True],
            [False, False, False],
        ]
        self.assertEqual( views.evolve_request(blinker_vertical), blinker_horizontal)








