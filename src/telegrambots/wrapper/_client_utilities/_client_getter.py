from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import TelegramBotsClient


class ClientGetter:
    """
    A class that provides a way to access the client instance
    """

    @property
    def client(self) -> 'TelegramBotsClient':
        """
        Returns the client instance
        """
        if hasattr(self, '_client'):
            return getattr(self, '_client')
        raise AttributeError('Client not set')
