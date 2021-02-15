class AuthenticationError(Exception):
    """Raised when our attempt to authenticate fails"""
    def __init__(self, message, response):
        self.response = response
        super(AuthenticationError, self).__init__(message)
