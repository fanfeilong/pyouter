class NotFound(Exception):
    def __init__(self, route, token):
        self.route = route
        self.token = token
        self.message = f"token [{token}] not found in {route}"