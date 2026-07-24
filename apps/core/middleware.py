class NoCacheForAuthenticatedUsersMiddleware:
    """Keep private portal screens out of browser history caches."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and not response.has_header("Cache-Control"):
            response["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
            response["Pragma"] = "no-cache"
            response["Expires"] = "0"
        return response
