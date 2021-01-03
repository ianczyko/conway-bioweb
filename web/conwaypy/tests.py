## @file calcpy/tests.py
#  @brief c++ calculation library Python API unit testing

import time
import django.test
import json
from django.http import JsonResponse


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
        self.assertEqual( conway.evolve(blinker_vertical, 1), blinker_horizontal )

class MyRequest:
    pass

class ConwayPyViewTestCase(django.test.TestCase):
    """module view test"""

    def test01getNumber(self):
        """check if service return proper dict"""
        request = MyRequest()
        request.body = json.dumps({
            'grid': [
                [False, True, False],
                [False, True, False],
                [False, True, False],
            ],
            'threads': 1
        }).encode('utf-8')
        blinker_horizontal = [
            [False, False, False],
            [True,  True,  True],
            [False, False, False],
        ]
        response = views.evolve_request(request)
        parsed = json.loads(response.content.decode('utf-8'))
        self.assertEqual( parsed['grid'], blinker_horizontal )








