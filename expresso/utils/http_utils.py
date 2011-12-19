import hashlib

from expresso.common.expresso_settings import EXPRESSO_PASSWORD_HASH
from expresso.utils.net_utils import get_query_param

def authorized_get_request(request_handler):
  def _authorized_get_request(*args, **kwargs):
    """Authorize the incoming HTTP Request.
    """
    if len(args) < 1:
      raise Exception("Please supply the web request")

    auth_token = get_query_param(args[0], 'auth_token')
    if auth_token is None:
      raise Exception('Please supply an authentication token')

    #TODO(inder)
    # Place genuine auth/session logic here
    if hashlib.sha224(auth_token).hexdigest() != EXPRESSO_PASSWORD_HASH:
      raise Exception("Unauthorized")

    return request_handler(*args, **kwargs)
  return _authorized_get_request
