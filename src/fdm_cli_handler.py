from cloudshell.cli.configurator import AbstractModeConfigurator
from cloudshell.cli.service.cli import CLI, SessionPoolManager
from cloudshell.cli.service.command_mode import CommandMode


class FDMCliHandler(AbstractModeConfigurator):
    @property
    def enable_mode(self):
        return CommandMode(r">\s*$")

    @property
    def config_mode(self):
        return CommandMode(r">\s*$")

    CLI = None

    @staticmethod
    def set_cli_session_pool_size(session_pool_size, session_pool_timeout=100):
        session_pool = SessionPoolManager(max_pool_size=session_pool_size, pool_timeout=session_pool_timeout)
        FDMCliHandler.CLI = CLI(session_pool)
