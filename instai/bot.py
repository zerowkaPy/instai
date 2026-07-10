from .fsm.storages.redis_storage import RedisStorage

class InstaBot:
    def __init__(
        self,
        access_token: str,
        ig_id: str,
        storage: RedisStorage):

        self.token = access_token
        self.my_id = ig_id
        self.storage = storage