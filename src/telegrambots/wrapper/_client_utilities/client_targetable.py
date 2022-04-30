from ._client_getter import ClientGetter
from ._client_setter import ClientSetter


class ClientTargetable(ClientGetter, ClientSetter):
    """
    This class is used to set the target of the client.
    """
