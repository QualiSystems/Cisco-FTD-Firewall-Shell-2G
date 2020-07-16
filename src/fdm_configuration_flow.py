from cloudshell.shell.flows.configuration.basic_flow import AbstractConfigurationFlow
from cloudshell.shell.flows.utils.networking_utils import UrlParser


class FDMConfigurationFlow(AbstractConfigurationFlow):
    def __init__(self, logger, resource_config, api_handler):
        """

        :type api_handler: fdm_rest_handler.FDMRestAPIHandler
        """
        super().__init__(logger, resource_config)
        self._api_handler = api_handler

    def _save_flow(self, folder_path, configuration_type, vrf_management_name):
        folder_path_details = UrlParser(folder_path)
        body = {
          "scheduleType": "IMMEDIATE",
          "user": self.resource_config.user,
          "forceOperation": True,
          "diskFileName": folder_path_details.FILENAME,
          "encryptionKey": "",
          "doNotEncrypt": True,
          "configExportType": "FULL_EXPORT",
          "deployedObjectsOnly": True,
          "type": "scheduleconfigexport"
        }
        self._api_handler.post("/action/configexport", body)

    def _restore_flow(self, path, configuration_type, restore_method, vrf_management_name):
        pass

    @property
    def _file_system(self):
        return "Local"
