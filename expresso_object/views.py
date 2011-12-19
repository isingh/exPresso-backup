from django.http import HttpResponse

from expresso.utils.http_utils import authorized_get_request

@authorized_get_request
def index(request):
  return HttpResponse('test, page')
