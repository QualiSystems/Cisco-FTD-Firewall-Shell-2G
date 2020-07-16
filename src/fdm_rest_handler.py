from cisco_ftd_firewall_shell_2g.src.rest_json_client import RestJsonClient


class FDMRestAPIHandler:
    OAUTH_GRANT_TYPE = "password"

    def __init__(self, logger, resource_config):
        self.rest_client = RestJsonClient(resource_config.address)
        self._oauth_token = None
        self._resource_config = resource_config
        self._logger = logger

    @property
    def token(self):
        if not self._oauth_token:
            self._oauth_token = self._get_token()
        return self._oauth_token

    def _get_token(self):
        body = {
            "grant_type": self.OAUTH_GRANT_TYPE,
            "username": self._resource_config.user,
            "password": self._resource_config.password
        }
        response = self.rest_client.request_post("/api/fdm/v5/fdm/token",
                                                 body)
        return response.get("access_token")
