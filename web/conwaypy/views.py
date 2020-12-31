## @file conway/views.py
#  @brief conway library interface to client

"""
conway library interface to client

export conway results to client
"""
from . import conway
from django.http import JsonResponse

def evolve_request(request):
    """the conway evolve from C++ library"""
    grid = request.POST['grid']
    grid = conway.evolve(grid)
    response = {
        'grid' : grid
    }
    return JsonResponse(response)

