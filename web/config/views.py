## @file web/views.py
#  @brief main server interface to client

"""
main interface to server
"""

import django.http
import json
import traceback

#all modules should be imported here
import version
import version.views
import current
import current.views
import conwaypy
import conwaypy.views

## for test working server
def index(request):
    """for test working server"""
    return django.http.HttpResponse("MyApp server" )

def evolve_request_wrapper(request):
    return conwaypy.views.evolve_request(request)

def ajax(request, module, function):
    """dispatch ajax requests"""
    print(request)
    try:
        fun = getattr(getattr(globals()[str(module)], 'views'), str(function))
        data = json.dumps( fun(request.GET) )
        return django.http.HttpResponse(data, content_type='application/json')
    except Exception as e:
        return django.http.HttpResponseNotFound("myapp ajax error: " + str(traceback.format_exc()) )
    except:
        return django.http.HttpResponseNotFound("myapp ajax system error " )
