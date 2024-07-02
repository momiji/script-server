from auth import auth_base


class HeaderAuthenticator(auth_base.Authenticator):
    def __init__(self, user_header_name, groups_header_name):
        super().__init__()
        self.user_header_name = user_header_name
        self.groups_header_name = groups_header_name
        self._user_groups = {}

    def authenticate(self, request_handler):
        username = request_handler.get_argument('username')
        return username
    
    def get_current_user(self, request_handler):
        username = request_handler.request.headers.get(self.user_header_name)
        groups = request_handler.request.headers.get(self.groups_header_name, "")
        self._user_groups[username] = groups.split(" ")
        return username

    def perform_basic_auth(self, user, password):
        return True

    def get_groups(self, user, known_groups=None):
        return self._user_groups.get(user, [])
