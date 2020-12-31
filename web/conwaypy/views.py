## @file conway/views.py
#  @brief conway library interface to client

"""
conway library interface to client

export conway results to client
"""
from . import conway
from django.http import JsonResponse
import json

def evolve_request(request):
    """the conway evolve from C++ library"""
    # print(str(request.body))
    grid = json.loads(request.body.decode('utf-8'))['grid']
    grid = conway.evolve(grid)
    response = {
        'grid' : grid
    }
    return JsonResponse({'grid': grid})
