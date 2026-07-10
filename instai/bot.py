from .fsm.storages.base_storage import BaseStorage
from .fsm.storages import MemoryStorage

class Instai:
    def __init__(
        self,
        access_token: str,
        ig_id: str,
        storage: BaseStorage = MemoryStorage()):

        self.token = access_token
        self.my_id = ig_id
        self.storage = storage