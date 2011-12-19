"""Network related utility functions.
"""

def get_query_param(request, query_param):
  """Get the given query string from the incoming request.

  Args:
    request - The HttpRequest coming in to the server.
    query_param - The query string that needs to be retrieved.

  Returns:
    String containing the value of the query param, else None.
  """
  if query_param in request.GET:
    return request.GET[query_param]
  return None

